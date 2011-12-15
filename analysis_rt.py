import time
import modal
from analysis import RTOnsetAnalysis, OnsetAnalysisThread
import modal.detectionfunctions as df

run_thread = OnsetAnalysisThread()
odfs = [
    df.EnergyODF, df.SpectralDifferenceODF, df.ComplexODF,
    df.LPEnergyODF, df.LPSpectralDifferenceODF, df.LPComplexODF,
    df.PeakAmpDifferenceODF
]
frame_size = 2048
hop_size = 512
lp_order = 5
files = modal.list_onset_files()

for file in files:
    for odf in odfs:
        oa = RTOnsetAnalysis()
        oa.analysis_file = file
        oa.odf = odf()
        oa.odf.set_frame_size(frame_size)
        oa.odf.set_hop_size(hop_size)
        if issubclass(odf, modal.LinearPredictionODF):
            oa.odf.set_order(lp_order)
        run_thread.add(oa)

start_time = time.time()
print "Starting analysis."
print "Press return to stop after the current analysis run"
print 
run_thread.start()
while not run_thread.finished.isSet():
    if raw_input() == "":
        run_thread.finished.set()
run_thread.join()
run_time = time.time() - start_time
print "Total running time:", 
print int(run_time / 60), "mins,", 
print int(run_time % 60), "secs"

