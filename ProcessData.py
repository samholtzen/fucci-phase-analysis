from InitalCalculations import media_frame
import numpy as np
import utils as ut
import matplotlib as mp


def main():
    
    
    
    
    
    
    
    
    
    
    
def trim_array(cell_phases, media_frame):
    
    """
    Purpose:
        Input two numpy arrays of fluorescent protein data and trim them
        to just look at data after media change frame.
        
    
    Inputs:
        cell_phases [numpy char array]:A character array containing rows
        corresponding to single cell traces with each column representing
        a frame, and each element containing a cell's cell cycle phase at that
        particular frame
    
    
    """
    media_ind = media_frame-1
    mC_after_change = mCherrydata[:,media_ind:]
    mV_after_change = mVenusdata[:,media_ind:]
    
    return cell_phase_after_change


def count_phase_frames(cell_phases):
    """
    Purpose:
        To count the number of frames a cell spends in each phase after
        changing the media.
        
    
    Inputs:
        A character array containing rows corresponding to single cell traces
        with each column represneting a frame, and each element containing
        a cell's cell cycle phase at that particular frame



    Outputs:
        A mixed character/integer vector containing in the first row a cell's
        phase, in the second row the cell's time spent in that phase
    """
    
    
    
    
    
    return 
    
