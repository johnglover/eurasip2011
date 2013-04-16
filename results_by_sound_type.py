import h5py
import modal


def f_measure(correctly_detected, false_positives, false_negatives):
    if not correctly_detected:
        return 0.0
    precision = correctly_detected / (correctly_detected + false_positives)
    recall = correctly_detected / (correctly_detected + false_negatives)
    return (2.0 * recall * precision) / (precision + recall)


# plot f-measure results for each sound type for this ODF
odf = 'LPSpectralDifferenceODF'

num_onsets = modal.num_onsets()
match_time = 50

onsets_db = h5py.File(modal.onsets_path, 'r')
db = h5py.File('results.hdf5', 'r')

try:
    results = {}
    sound_type_count = {}

    for file in db['files']:
        for analysis in db['files'][file]:
            if not db['files'][file][analysis].attrs['odf_type'] == odf:
                continue

            file_results = db['files'][file][analysis][str(match_time)]

            cd = float(file_results.attrs['correctly_detected'])
            fp = float(file_results.attrs['false_positives'])
            fn = float(file_results.attrs['false_negatives'])
            f = f_measure(cd, fp, fn)

            sound_type = onsets_db[file].attrs['type']
            if not sound_type in results:
                results[sound_type] = f
                sound_type_count[sound_type] = 1
            else:
                results[sound_type] += f
                sound_type_count[sound_type] += 1

    for sound_type in results:
        results[sound_type] /= sound_type_count[sound_type]

finally:
    db.close()

print 'Average F-Measures for {0}:'.format(odf)
for sound_type in results:
    print '{0}: {1}'.format(sound_type, results[sound_type])
