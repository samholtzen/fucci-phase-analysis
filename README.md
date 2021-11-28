# fucci-phase-analysis
A toolbox for analyzing live-cell imaging data using the Fluorescent Ubiquitination Cell Cycle Indicator (FUCCI).
Takes in two .csv files (one for mVenus intensity, one for mCherry intensity) and returns graphs of the
cell cycle phases at each frame of the live-cell movie. 

# Utils.py
A utility toolbox that is used to read in files, and make basic calculations that will be repeated over the course of a single analysis.

# InitialCalculations.py
A script that takes input of two fluorescence intensity csv files and finds the derivative and ratios of them. 

