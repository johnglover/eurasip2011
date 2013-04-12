Real-time Detection of Musical Onsets with Linear Prediction and Sinusoidal Modelling - EURASIP 2011
====================================================================================================

Code needed to replicate the results from my 2011 paper in the open access
EURASIP Journal on Advances in Signal Processing.

The article (and reference information) can be found here:
http://asp.eurasipjournals.com/content/2011/1/68

Send comments/queries to john dot c dot glover at nuim dot ie


Dependencies
------------

* [Modal](http://github.com/johnglover/modal) (and all related dependencies)


Modal Onset Database
--------------------

The most recent onset database (set of annotated samples) is
[available from Dropbox](http://dl.dropbox.com/u/9444913/onsets1.1.hdf5)


Use
---

Make sure that the variable `data_path` in the main `__init__.py` file
corresponds to the directory that your modal onset database is in, and that
`onsets_path` corresponds to the name of the onset database.
This defaults to the `data` folder in the package directory.

Run:

    $ python analysis.py

This will create a HDF5 file containing the analysis results called
`analysis.hdf5` in the same directory.

After making an analysis database, run

    $ python results.py

to build a results database.

Running

    $ python plot_results.py

will create plots of the precision, recall and f-measure results
in a directory called ``images``.
