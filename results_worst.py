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
        worst_hop_size = {}
        worst_frame_size = {}
        worst_prediction_frames = {}

        for odf in odfs:
            worst = 10.0
            for analysis in db['totals/analysis']:
                if db['totals/analysis'][analysis].attrs['odf_type'] == odf:
                    a = db['totals/analysis'][analysis]
                    if a.attrs['f_measure'] < worst:
                        worst = a.attrs['f_measure']
                        worst_hop_size[odf] = str(a.attrs['hop_size'])
                        worst_frame_size[odf] = str(a.attrs['frame_size'])
                        if 'prediction_frames' in a.attrs:
                            worst_prediction_frames[odf] = str(
                                a.attrs['prediction_frames']
                            )
                        else:
                            worst_prediction_frames[odf] = ''
                    elif a.attrs['f_measure'] == worst:
                        worst_hop_size[odf] += ', ' + str(a.attrs['hop_size'])
                        worst_frame_size[odf] += ', ' + \
                            str(a.attrs['frame_size'])
                        if 'prediction_frames' in a.attrs:
                            worst_prediction_frames[odf] += ', ' + \
                                str(a.attrs['prediction_frames'])
            results[odf] = worst

        for odf in odfs:
            print odf + ':'
            print 'f:', results[odf]
            print 'hop size:', worst_hop_size[odf]
            print 'frame size:', worst_frame_size[odf]
            print 'prediction frames:', worst_prediction_frames[odf]
            print

        if plot_results:
            image_file = 'images/worst_f_measure.png'
            results = [results[odf] for odf in odfs]

            indexes = np.arange(len(odfs))
            width = 0.8
            colours, styles = scheme(len(odfs))
            fig = plt.figure(2, figsize=(12, 8))
            plt.title('Worst F-Measure')
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
        worst_hop_size = {}
        worst_frame_size = {}
        worst_prediction_frames = {}

        for odf in odfs:
            worst = 10.0
            for analysis in db['totals/analysis']:
                if db['totals/analysis'][analysis].attrs['odf_type'] == odf:
                    a = db['totals/analysis'][analysis]
                    if a.attrs['precision'] < worst:
                        worst = a.attrs['precision']
                        worst_hop_size[odf] = str(a.attrs['hop_size'])
                        worst_frame_size[odf] = str(a.attrs['frame_size'])
                        if 'prediction_frames' in a.attrs:
                            worst_prediction_frames[odf] = str(
                                a.attrs['prediction_frames']
                            )
                        else:
                            worst_prediction_frames[odf] = ''
                    elif a.attrs['precision'] == worst:
                        worst_hop_size[odf] += ', ' + \
                            str(a.attrs['hop_size'])
                        worst_frame_size[odf] += ', ' + \
                            str(a.attrs['frame_size'])
                        if 'prediction_frames' in a.attrs:
                            worst_prediction_frames[odf] += ', ' + \
                                str(a.attrs['prediction_frames'])
            results[odf] = worst

        for odf in odfs:
            print odf + ':'
            print 'precision:', results[odf]
            print 'hop size:', worst_hop_size[odf]
            print 'frame size:', worst_frame_size[odf]
            print 'prediction frames:', worst_prediction_frames[odf]
            print

        if plot_results:
            image_file = 'images/worst_precision.png'
            results = [results[odf] for odf in odfs]

            indexes = np.arange(len(odfs))
            width = 0.8
            colours, styles = scheme(len(odfs))
            fig = plt.figure(3, figsize=(12, 8))
            plt.title('Worst Precision')
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
        worst_hop_size = {}
        worst_frame_size = {}
        worst_prediction_frames = {}

        for odf in odfs:
            worst = 10.0
            for analysis in db['totals/analysis']:
                if db['totals/analysis'][analysis].attrs['odf_type'] == odf:
                    a = db['totals/analysis'][analysis]
                    if a.attrs['recall'] < worst:
                        worst = a.attrs['recall']
                        worst_hop_size[odf] = str(a.attrs['hop_size'])
                        worst_frame_size[odf] = str(a.attrs['frame_size'])
                        if 'prediction_frames' in a.attrs:
                            worst_prediction_frames[odf] = str(
                                a.attrs['prediction_frames']
                            )
                        else:
                            worst_prediction_frames[odf] = ''
                    elif a.attrs['recall'] == worst:
                        worst_hop_size[odf] += ', ' + str(a.attrs['hop_size'])
                        worst_frame_size[odf] += ', ' + \
                            str(a.attrs['frame_size'])
                        if 'prediction_frames' in a.attrs:
                            worst_prediction_frames[odf] += ', ' + \
                                str(a.attrs['prediction_frames'])
            results[odf] = worst

        for odf in odfs:
            print odf + ':'
            print 'recall:', results[odf]
            print 'hop size:', worst_hop_size[odf]
            print 'frame size:', worst_frame_size[odf]
            print 'prediction frames:', worst_prediction_frames[odf]
            print

        if plot_results:
            image_file = 'images/worst_recall.png'
            results = [results[odf] for odf in odfs]

            indexes = np.arange(len(odfs))
            width = 0.8
            colours, styles = scheme(len(odfs))
            fig = plt.figure(4, figsize=(12, 8))
            plt.title('Worst Recall')
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
        worst_hop_size = {}
        worst_frame_size = {}
        worst_prediction_frames = {}

        for odf in odfs:
            worst = 0.0
            for analysis in db['totals/analysis']:
                if db['totals/analysis'][analysis].attrs['odf_type'] == odf:
                    a = db['totals/analysis'][analysis]
                    if a.attrs['false_positive_rate'] > worst:
                        worst = a.attrs['false_positive_rate']
                        worst_hop_size[odf] = str(a.attrs['hop_size'])
                        worst_frame_size[odf] = str(a.attrs['frame_size'])
                        if 'prediction_frames' in a.attrs:
                            worst_prediction_frames[odf] = str(
                                a.attrs['prediction_frames']
                            )
                        else:
                            worst_prediction_frames[odf] = ''
                    elif a.attrs['false_positive_rate'] == worst:
                        worst_hop_size[odf] += ', ' + str(a.attrs['hop_size'])
                        worst_frame_size[odf] += ', ' + \
                            str(a.attrs['frame_size'])
                        if 'prediction_frames' in a.attrs:
                            worst_prediction_frames[odf] += ', ' + \
                                str(a.attrs['prediction_frames'])
            results[odf] = worst

        for odf in odfs:
            print odf + ':'
            print 'false positive rate:', results[odf]
            print 'hop size:', worst_hop_size[odf]
            print 'frame size:', worst_frame_size[odf]
            print 'prediction frames:', worst_prediction_frames[odf]
            print

        if plot_results:
            image_file = 'images/worst_false_positive_rate.png'
            results = [results[odf] for odf in odfs]

            indexes = np.arange(len(odfs))
            width = 0.8
            colours, styles = scheme(len(odfs))
            fig = plt.figure(5, figsize=(12, 8))
            plt.title('Worst False Positive Rate')
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
