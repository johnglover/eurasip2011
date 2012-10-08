import os
import h5py
import numpy as np
import matplotlib.pyplot as plt
import modal
from modal.ui.plot import scheme

# plot results to files?
plot_results = True

# result types to calculate
f_measure = True
precision = True
recall = True
false_positive_rate = True

# ODFs to include in results
odfs = ['EnergyODF', 'SpectralDifferenceODF', 'ComplexODF', 'LPEnergyODF',
        'LPSpectralDifferenceODF', 'LPComplexODF', 'PeakAmpDifferenceODF']

# shorter names for plotting
odf_names = ['Energy', 'SpecDiff', 'Complex',
             'LPE', 'LPSD', 'LPCD', 'PAD']

num_onsets = modal.num_onsets()
db = h5py.File('results.hdf5', 'r')

if plot_results:
    if not os.path.exists('images'):
        os.mkdir('images')

try:
    # F measure
    if f_measure:
        results = {}
        best_hop_size = {}
        best_frame_size = {}
        best_prediction_frames = {}

        for odf in odfs:
            best = 0.0
            for analysis in db['totals/analysis']:
                if db['totals/analysis'][analysis].attrs['odf_type'] == odf:
                    a = db['totals/analysis'][analysis]
                    if a.attrs['f_measure'] > best:
                        best = a.attrs['f_measure']
                        best_hop_size[odf] = str(a.attrs['hop_size'])
                        best_frame_size[odf] = str(a.attrs['frame_size'])
                        if 'prediction_frames' in a.attrs:
                            best_prediction_frames[odf] = str(
                                a.attrs['prediction_frames']
                            )
                        else:
                            best_prediction_frames[odf] = ''
                    elif a.attrs['f_measure'] == best:
                        best_hop_size[odf] += ', ' + str(a.attrs['hop_size'])
                        best_frame_size[odf] += ', ' + \
                            str(a.attrs['frame_size'])
                        if 'prediction_frames' in a.attrs:
                            best_prediction_frames[odf] += ', ' + \
                                str(a.attrs['prediction_frames'])
            results[odf] = best

        for odf in odfs:
            print odf + ':'
            print 'f:', results[odf]
            print 'hop size:', best_hop_size[odf]
            print 'frame size:', best_frame_size[odf]
            print 'prediction frames:', best_prediction_frames[odf]
            print

        if plot_results:
            image_file = 'images/best_f_measure.png'
            results = [results[odf] for odf in odfs]

            indexes = np.arange(len(odfs))
            width = 0.8
            colours, styles = scheme(len(odfs))
            fig = plt.figure(2, figsize=(12, 8))
            plt.title('Best F-Measure')
            ax = plt.axes()
            ax.autoscale(False, 'y')
            ax.set_ylim(0.0, 1.4)
            bars = ax.bar(indexes, results, width, color=colours[0])
            for bar in bars:
                height = bar.get_height()
                ax.text(bar.get_x() + bar.get_width() / 2., 1.05 * height,
                        '%f' % height, ha='center', va='bottom')
            ax.set_ylabel('F-Measure')
            ax.set_xlabel('Detection Functions')
            ax.set_xticks(indexes + 0.4)
            ax.set_xticklabels(odf_names)
            plt.savefig(image_file, bbox_inches='tight')

    # Precision
    if precision:
        results = {}
        best_hop_size = {}
        best_frame_size = {}
        best_prediction_frames = {}

        for odf in odfs:
            best = 0.0
            for analysis in db['totals/analysis']:
                if db['totals/analysis'][analysis].attrs['odf_type'] == odf:
                    a = db['totals/analysis'][analysis]
                    if a.attrs['precision'] > best:
                        best = a.attrs['precision']
                        best_hop_size[odf] = str(a.attrs['hop_size'])
                        best_frame_size[odf] = str(a.attrs['frame_size'])
                        if 'prediction_frames' in a.attrs:
                            best_prediction_frames[odf] = str(
                                a.attrs['prediction_frames']
                            )
                        else:
                            best_prediction_frames[odf] = ''
                    elif a.attrs['precision'] == best:
                        best_hop_size[odf] += ', ' + str(a.attrs['hop_size'])
                        best_frame_size[odf] += ', ' + \
                            str(a.attrs['frame_size'])
                        if 'prediction_frames' in a.attrs:
                            best_prediction_frames[odf] += ', ' + \
                                str(a.attrs['prediction_frames'])
            results[odf] = best

        for odf in odfs:
            print odf + ':'
            print 'precision:', results[odf]
            print 'hop size:', best_hop_size[odf]
            print 'frame size:', best_frame_size[odf]
            print 'prediction frames:', best_prediction_frames[odf]
            print

        if plot_results:
            image_file = 'images/best_precision.png'
            results = [results[odf] for odf in odfs]

            indexes = np.arange(len(odfs))
            width = 0.8
            colours, styles = scheme(len(odfs))
            fig = plt.figure(3, figsize=(12, 8))
            plt.title('Best Precision')
            ax = plt.axes()
            ax.autoscale(False, 'y')
            ax.set_ylim(0.0, 1.4)
            bars = ax.bar(indexes, results, width, color=colours[0])
            for bar in bars:
                height = bar.get_height()
                ax.text(bar.get_x() + bar.get_width() / 2., 1.05 * height,
                        '%f' % height, ha='center', va='bottom')
            ax.set_ylabel('Precision')
            ax.set_xlabel('Detection Functions')
            ax.set_xticks(indexes + 0.4)
            ax.set_xticklabels(odf_names)
            plt.savefig(image_file, bbox_inches='tight')

    # Recall
    if recall:
        results = {}
        best_hop_size = {}
        best_frame_size = {}
        best_prediction_frames = {}

        for odf in odfs:
            best = 0.0
            for analysis in db['totals/analysis']:
                if db['totals/analysis'][analysis].attrs['odf_type'] == odf:
                    a = db['totals/analysis'][analysis]
                    if a.attrs['recall'] > best:
                        best = a.attrs['recall']
                        best_hop_size[odf] = str(a.attrs['hop_size'])
                        best_frame_size[odf] = str(a.attrs['frame_size'])
                        if 'prediction_frames' in a.attrs:
                            best_prediction_frames[odf] = str(
                                a.attrs['prediction_frames']
                            )
                        else:
                            best_prediction_frames[odf] = ''
                    elif a.attrs['recall'] == best:
                        best_hop_size[odf] += ', ' + str(a.attrs['hop_size'])
                        best_frame_size[odf] += ', ' + \
                            str(a.attrs['frame_size'])
                        if 'prediction_frames' in a.attrs:
                            best_prediction_frames[odf] += ', ' + \
                                str(a.attrs['prediction_frames'])
            results[odf] = best

        for odf in odfs:
            print odf + ':'
            print 'recall:', results[odf]
            print 'hop size:', best_hop_size[odf]
            print 'frame size:', best_frame_size[odf]
            print 'prediction frames:', best_prediction_frames[odf]
            print

        if plot_results:
            image_file = 'images/best_recall.png'
            results = [results[odf] for odf in odfs]

            indexes = np.arange(len(odfs))
            width = 0.8
            colours, styles = scheme(len(odfs))
            fig = plt.figure(4, figsize=(12, 8))
            plt.title('Best Recall')
            ax = plt.axes()
            ax.autoscale(False, 'y')
            ax.set_ylim(0.0, 1.4)
            bars = ax.bar(indexes, results, width, color=colours[0])
            for bar in bars:
                height = bar.get_height()
                ax.text(bar.get_x() + bar.get_width() / 2., 1.05 * height,
                        '%f' % height, ha='center', va='bottom')
            ax.set_ylabel('Recall')
            ax.set_xlabel('Detection Functions')
            ax.set_xticks(indexes + 0.4)
            ax.set_xticklabels(odf_names)
            plt.savefig(image_file, bbox_inches='tight')

    # False positive rate
    if false_positive_rate:
        results = {}
        best_hop_size = {}
        best_frame_size = {}
        best_prediction_frames = {}

        for odf in odfs:
            best = 500.0
            for analysis in db['totals/analysis']:
                if db['totals/analysis'][analysis].attrs['odf_type'] == odf:
                    a = db['totals/analysis'][analysis]
                    if a.attrs['false_positive_rate'] < best:
                        best = a.attrs['false_positive_rate']
                        best_hop_size[odf] = str(a.attrs['hop_size'])
                        best_frame_size[odf] = str(a.attrs['frame_size'])
                        if 'prediction_frames' in a.attrs:
                            best_prediction_frames[odf] = str(
                                a.attrs['prediction_frames']
                            )
                        else:
                            best_prediction_frames[odf] = ''
                    elif a.attrs['false_positive_rate'] == best:
                        best_hop_size[odf] += ', ' + str(a.attrs['hop_size'])
                        best_frame_size[odf] += ', ' + \
                            str(a.attrs['frame_size'])
                        if 'prediction_frames' in a.attrs:
                            best_prediction_frames[odf] += ', ' + \
                                str(a.attrs['prediction_frames'])
            results[odf] = best

        for odf in odfs:
            print odf + ':'
            print 'false positive rate:', results[odf]
            print 'hop size:', best_hop_size[odf]
            print 'frame size:', best_frame_size[odf]
            print 'prediction frames:', best_prediction_frames[odf]
            print

        if plot_results:
            image_file = 'images/best_false_positive_rate.png'
            results = [results[odf] for odf in odfs]

            indexes = np.arange(len(odfs))
            width = 0.8
            colours, styles = scheme(len(odfs))
            fig = plt.figure(5, figsize=(12, 8))
            plt.title('Best False Positive Rate')
            ax = plt.axes()
            ax.autoscale(False, 'y')
            ax.set_ylim(0.0, 100.0)
            bars = ax.bar(indexes, results, width, color=colours[0])
            for bar in bars:
                height = bar.get_height()
                ax.text(bar.get_x() + bar.get_width() / 2., 1.05 * height,
                        '%f' % height, ha='center', va='bottom')
            ax.set_ylabel('False Positive Rate')
            ax.set_xlabel('Detection Functions')
            ax.set_xticks(indexes + 0.4)
            ax.set_xticklabels(odf_names)
            plt.savefig(image_file, bbox_inches='tight')
finally:
    db.close()
