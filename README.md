# fucci-phase-analysis
###Developed by Sam Holtzen, Payton Martinez, Sai Samineni for Sam Holtzen's Thesis Project

A toolbox for analyzing live-cell imaging data using the Fluorescent Ubiquitination Cell Cycle Indicator (FUCCI CA).
Takes in two .csv files (one for mVenus intensity, one for mCherry intensity) and returns graphs of the
cell cycle phase distribution at each frame of the live-cell movie. 

##Method
This pipeline takes advantage of a Support Vector Machine (SVM), trained on data to segregate cells roughly into phases.

The predictions from the SVM are then cleaned according to cell cycle phase progression (G1, S, G2, M) and data is
returned as a list of string values corresponding to phases.


# Utils.py
A utility toolbox that is used to read in files, and make basic calculations that will be repeated over the course of a single analysis.


