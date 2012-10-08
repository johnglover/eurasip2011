import os
import h5py
import numpy as np
import modal
from modal.ui.plot import scheme
import matplotlib.pyplot as plt
from matplotlib import rc

# plot results to files?
plot_results = True

# result types to calculate
f_measure = True
precision = True
recall = True
false_positive_rate = False

# ODFs to include in results
odfs = ['EnergyODF', 'SpectralDifferenceODF', 'ComplexODF', 'LPEnergyODF',
        'LPSpectralDifferenceODF', 'LPComplexODF', 'PeakAmpDifferenceODF']

# shorter names for plotting
odf_names = ["E", "SD", "CD", "ELP", "SDLP", "CDLP", "PAD"]
# odf_names = [r'$\text{ODF}_{\rm E}$', r'$\text{ODF}_{\rm SD}$',
#              r'$\text{ODF}_{\rm CD}$', r'$\text{ODF}_{\rm ELP}$',
#              r'$\text{ODF}_{\rm SDLP}$', r'$\text{ODF}_{\rm CDLP}$',
#              r'$\text{ODF}_{\rm PAD}$']

num_onsets = modal.num_onsets()
db = h5py.File('results.hdf5', 'r')
rc('text', usetex=True)

if plot_results:
    if not os.path.exists('images'):
        os.mkdir('images')

try:
    # F-Measure
    if f_measure:
        results = {}
        for odf in odfs:
            results[odf] = db['totals/odfs'][odf].attrs['f_measure']

        if plot_results:
            image_file = 'images/avg_f_measure.png'
            results = [results[odf] for odf in odfs]
            indexes = np.arange(len(odfs))
            width = 0.8
            colours, styles = scheme(len(odfs), 2)
            fig = plt.figure(2, figsize=(14, 9))
            plt.title('Average F-Measure')
            ax = plt.axes()
            ax.autoscale(False, 'y')
            ax.set_ylim(0.0, 1.0)
            bars = ax.bar(indexes, results, width, color=colours)
            for bar in bars:
                height = bar.get_height()
                ax.text(bar.get_x() + bar.get_width() / 2., 1.05 * height,
                        '%.2f' % height, ha='center', va='bottom')
            ax.set_ylabel('F-measure')
            ax.set_xlabel('Detection Functions')
            ax.set_xticks(indexes + 0.4)
            ax.set_xticklabels(odf_names)
            plt.savefig(image_file, bbox_inches='tight')

    # Precision
    if precision:
        results = {}
        for odf in odfs:
            results[odf] = db['totals/odfs'][odf].attrs['precision']

        if plot_results:
            image_file = 'images/avg_precision.png'
            results = [results[odf] for odf in odfs]
            indexes = np.arange(len(odfs))
            width = 0.8
            colours, styles = scheme(len(odfs), 2)
            fig = plt.figure(3, figsize=(14, 9))
            plt.title('Average Precision')
            ax = plt.axes()
            ax.autoscale(False, 'y')
            ax.set_ylim(0.0, 1.0)
            bars = ax.bar(indexes, results, width, color=colours)
            for bar in bars:
                height = bar.get_height()
                ax.text(bar.get_x() + bar.get_width() / 2., 1.05 * height,
                        '%.2f' % height, ha='center', va='bottom')
            ax.set_ylabel('Precision')
            ax.set_xlabel('Detection Functions')
            ax.set_xticks(indexes + 0.4)
            ax.set_xticklabels(odf_names)
            plt.savefig(image_file, bbox_inches='tight')

    # Recall
    if recall:
        results = {}
        for odf in odfs:
            results[odf] = db['totals/odfs'][odf].attrs['recall']

        if plot_results:
            image_file = 'images/avg_recall.png'
            results = [results[odf] for odf in odfs]
            indexes = np.arange(len(odfs))
            width = 0.8
            colours, styles = scheme(len(odfs), 2)
            fig = plt.figure(4, figsize=(14, 9))
            plt.title('Average Recall')
            ax = plt.axes()
            ax.autoscale(False, 'y')
            ax.set_ylim(0.0, 1.0)
            bars = ax.bar(indexes, results, width, color=colours)
            for bar in bars:
                height = bar.get_height()
                ax.text(bar.get_x() + bar.get_width() / 2., 1.05 * height,
                        '%.2f' % height, ha='center', va='bottom')
            ax.set_ylabel('Recall')
            ax.set_xlabel('Detection Functions')
            ax.set_xticks(indexes + 0.4)
            ax.set_xticklabels(odf_names)
            plt.savefig(image_file, bbox_inches='tight')

    # False positive rate
    if false_positive_rate:
        results = {}
        for odf in odfs:
            results[odf] = db['totals/odfs'][odf].attrs['false_positive_rate']

        if plot_results:
            image_file = 'images/avg_false_positive_rate.png'
            results = [results[odf] for odf in odfs]
            indexes = np.arange(len(odfs))
            width = 0.8
            colours, styles = scheme(len(odfs), 2)
            fig = plt.figure(5, figsize=(14, 9))
            plt.title('Average False Positive Rate')
            ax = plt.axes()
            ax.autoscale(False, 'y')
            ax.set_ylim(0.0, 100.0)
            bars = ax.bar(indexes, results, width, color=colours)
            for bar in bars:
                height = bar.get_height()
                ax.text(bar.get_x() + bar.get_width() / 2., 1.05 * height,
                        '%.2f' % height, ha='center', va='bottom')
            ax.set_ylabel('False Positive Rate')
            ax.set_xlabel('Detection Functions')
            ax.set_xticks(indexes + 0.4)
            ax.set_xticklabels(odf_names)
            plt.savefig(image_file, bbox_inches='tight')
finally:
    db.close()
