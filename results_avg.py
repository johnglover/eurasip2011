import os
import h5py
import numpy as np
import modal
from modal.ui.plot import scheme
import matplotlib.pyplot as plt
from matplotlib import rc


def plot_bars(file, results, labels, title, x_label, y_label):
    indexes = np.arange(len(results))
    width = 0.8
    colours, styles = scheme(len(results), 2)
    plt.clf()
    plt.figure(1, figsize=(14, 9))
    plt.title(title, fontsize=20)
    ax = plt.axes()
    ax.autoscale(False, 'y')
    ax.set_ylim(0.0, 1.0)
    bars = ax.bar(indexes, results, width, color=colours)
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2., 1.05 * height,
                '%.2f' % height, ha='center', va='bottom',
                fontsize=18)
    ax.set_ylabel(y_label, fontsize=18)
    ax.set_xlabel(x_label, fontsize=18)
    ax.set_xticks(indexes + 0.4)
    ax.set_xticklabels(labels, fontsize=14)
    plt.savefig(file, bbox_inches='tight')


# plot results to files?
plot_results = True

# result types to calculate
f_measure = True
precision = True
recall = True

# ODFs to include in results
odfs = ['EnergyODF', 'SpectralDifferenceODF', 'ComplexODF', 'LPEnergyODF',
        'LPSpectralDifferenceODF', 'LPComplexODF', 'PeakAmpDifferenceODF']

# shorter names for plotting
odf_names = ['E', 'SD', 'CD', 'ELP', 'SDLP', 'CDLP', 'PAD']
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
    if f_measure:
        results = {}
        for odf in odfs:
            results[odf] = db['totals/odfs'][odf].attrs['f_measure']

        if plot_results:
            results = [results[odf] for odf in odfs]
            plot_bars('images/avg_f_measure.png', results, odf_names,
                      'Average F-Measure', 'Detection Functions', 'F-Measure')

    if precision:
        results = {}
        for odf in odfs:
            results[odf] = db['totals/odfs'][odf].attrs['precision']

        if plot_results:
            results = [results[odf] for odf in odfs]
            plot_bars('images/avg_precision.png', results, odf_names,
                      'Average Precision', 'Detection Functions', 'Precision')

    if recall:
        results = {}
        for odf in odfs:
            results[odf] = db['totals/odfs'][odf].attrs['recall']

        if plot_results:
            results = [results[odf] for odf in odfs]
            plot_bars('images/avg_recall.png', results, odf_names,
                      'Average Recall', 'Detection Functions', 'Recall')
finally:
    db.close()
