from InitalCalculations import media_frame
import numpy as np
import utils as ut
import matplotlib as mp


def main():
    
    
    
    
    
    
    
    
    
    
    
def trim_array(cell_phases, media_frame):
    
    '''
    Purpose:
        Input two numpy arrays of fluorescent protein data and trim them
        to just look at data after media change frame.
        
    
    Inputs:
        cell_phases [numpy char array]:A character array containing rows
        corresponding to single cell traces with each column representing
        a frame, and each element containing a cell's cell cycle phase at that
        particular frame
    
    
    '''
    media_ind = media_frame-1
    mC_after_change = mCherrydata[:,media_ind:]
    mV_after_change = mVenusdata[:,media_ind:]
    
    return cell_phase_after_change


def count_phase_frames(cell_phases):
    '''
    Purpose:
        To count the number of frames a cell spends in each phase after
        changing the media.
        
    
    Inputs:
        A character array containing rows corresponding to single cell traces
        with each column represneting a frame, and each element containing
        a cell's cell cycle phase at that particular frame



    Outputs:
        Three lists of lists, containing the time spent in each phase in the
        sublist, with each element in the larger list corresponding to the
        tracks
    '''
    all_G1_lengths = []
    all_S_lengths = []
    all_G2_lengths = []
    
    for cell in cell_phases:
        
        # Convert the numpy array to one long string
        cellstr_temp = ''.join(cell_phases[cell])
        
        # Split the array into individual cells by split string at 'M'
        cell_split = cellstr_temp.split('M')
        
        
        G1_lengths = []
        S_lengths = []
        G2_lengths = []
        
        for i in cell_phases:
            
            # Loop through and find the number of instances of "G1"
            G1_length = cell_split[i].count('G1')
            G1_lengths.append(G1_length)
            
            S_length = cell_split[i].count('S')
            S_lengths.append(S_length)
            
            G2_length = cell_split[i].count('G2')
            G2_lengths.append(G2_length)
        
    all_G1_lengths.append(G1_lengths)
    all_S_lengths.append(S_lengths)
    all_G2_lengths.append(G2_lengths)
    
    return all_G1_lengths, all_S_lengths, all_G2_lengths
    

def tpa_timing(cell_phases, media_frame):
    
    
    