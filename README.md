Real-time Detection of Musical Onsets with Linear Prediction and Sinusoidal Modelling - EURASIP 2011
====================================================================================================

Code needed to replicate the results from my 2011 paper in the open access EURASIP Journal on Advances in Signal Processing.

The article (and reference information) can be found here: http://asp.eurasipjournals.com/content/2011/1/68

Send comments/queries to john dot c dot glover at nuim dot ie


Dependencies
------------

* [Modal](http://github.com/johnglover/modal) (and all related dependencies)


Use
---

Make sure that the variable `data_path` in the main `__init__.py` file corresponds to the directory
that your modal onset database is in, and that `onsets_path` corresponds to the name of the onset database.
This defaults to the `data` folder in the package directory.

Run:

  $ python analysis_rt.py 

This will create a HDF5 file containing the analysis results called `analysis.hdf5` in the same directory.

After making an analysis database, run

  $ python results_compute.py
  
to build a results database. The files `results_avg.py`, `results_best.py` and `results_worst.py` can then be used to view average, 
best and worse case results respectively for all analysis data.

