import h5py
import modal


def f_measure(correctly_detected, false_positives, false_negatives):
    if not correctly_detected:
        return 0.0
    precision = correctly_detected / (correctly_detected + false_positives)
    recall = correctly_detected / (correctly_detected + false_negatives)
    return (2.0 * recall * precision) / (precision + recall)


odfs = ['EnergyODF',
        'SpectralDifferenceODF',
        'ComplexODF',
        'LPEnergyODF',
        'LPSpectralDifferenceODF',
        'LPComplexODF',
        'PeakAmpDifferenceODF']

sound_types = ['Non-Pitched Percussive',
               'Pitched Percussive',
               'Pitched Non-Percussive',
               'Mixed']

num_onsets = modal.num_onsets()
match_time = 50

onsets_db = h5py.File(modal.onsets_path, 'r')
db = h5py.File('results.hdf5', 'r')

results = {odf: {t: {'cd': 0.0, 'fp': 0.0, 'fn': 0.0} for t in sound_types}
           for odf in odfs}

try:

    for file in db['files']:
        for analysis in db['files'][file]:
            odf = db['files'][file][analysis].attrs['odf_type']

            file_results = db['files'][file][analysis][str(match_time)]
            cd = float(file_results.attrs['correctly_detected'])
            fp = float(file_results.attrs['false_positives'])
            fn = float(file_results.attrs['false_negatives'])

            sound_type = onsets_db[file].attrs['type']
            results[odf][sound_type]['cd'] += cd
            results[odf][sound_type]['fp'] += fp
            results[odf][sound_type]['fn'] += fn

finally:
    db.close()

for odf in odfs:
    print '{0}:'.format(odf)
    for t in sound_types:
        f = f_measure(results[odf][t]['cd'],
                      results[odf][t]['fp'],
                      results[odf][t]['fn'])
        print '{0}: {1:.2f}'.format(t, f)
    print
