from InitalCalculations import media_frame
import numpy as np
import utils as ut
import matplotlib as mp
import pandas as pd


def main():
    
    
    
    
    
    
    
    
    
    



def count_phase_frames(cell_phases, media_frame):
    '''
    Purpose:
        To count the number of frames a cell spends in each phase after
        changing the media.
        
    
    Inputs:
        A character array containing rows corresponding to single cell traces
        with each column represneting a frame, and each element containing
        a cell's cell cycle phase at that particular frame
        
        An integer represneitng frame at which the media was changed on 
        these cells


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
        
        cellstr_temp = cellstr_temp[media_frame:]
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


def media_timing(cell_phases, media_frame):
    '''
    Purpose:
        To determine at what point in a cell cycle phase a cell was in old
        media before being changed to the new one
        
    
    Inputs:
        A character array containing rows corresponding to single cell traces
        with each column represneting a frame, and each element containing
        a cell's cell cycle phase at that particular frame
        
        An int corresponding to the frame at which the media was changed


    Outputs:
        Two lists of lists, first containing the phase at which the
        media was changed, the second containing how long it was in that phase
        before the media was changed
    '''
    cell_phase_at_change = []
    time_in_phase_at_change = []
    
    for cell in cell_phases:
        
        time_in_phase = 1
        
        phase_at_change = cell[media_frame-1]
        frame_to_check = media_frame-2
        cell_phase_at_change.append(phase_at_change)
        
        while phase_before == phase_at_change:
            
            if phase_before > 2:
                
                phase_before = cell[frame_to_check]
                time_in_phase += 1
                frame_to_check -= 1
                
            else:
                
                break
        
        time_in_phase_at_change.append(time_in_phase)
    
    return cell_phase_at_change, time_in_phase_at_change


def get_cell_G1_stats(cell_phase_at_change, time_in_phase_at_change, all_G1_lengths):
        '''
    Purpose:
        To bin cells based on their fate and correlate this to their time in
        treatment media.
        
    
    Inputs:
        A list of strings with each element corresponding to the cell's phase
        at change
        
        A list of ints with each element corresponding to the cell's time 
        spent in the phase
        
        A list of lists containing how long each cell spends in the daughter
        cell G1s


    Outputs:
        Returning an n x 3 array, with each row corresponding to a cell
        column 1 is the phase of the cell at media change
        column 2 is frames into the phase the cell was before media change
        column 3 is how long the daughter G1 is 
        
    '''
    
    all_cell_G1_stats = []
    
    for i in range(len(cell_phase_at_change)):
        
        phase_temp = cell_phase_at_change[i]
        time_temp = time_in_phase_at_change[i]
        
        if phase_temp == 'G1':
            
            G1_temp = all_G1_lengths[1]
            
        else:
            
            G1_temp = all_G1_lengths[0]
            
        cell_temp = [phase_temp,time_temp_G1_temp]
        
        all_cells_G1_stats.append(cell_temp)
        

    return all_cells_G1_stats
    
    
def get_cell_S_stats(cell_phase_at_change, time_in_phase_at_change, all_S_lengths):
        '''
    Purpose:
        To bin cells based on their fate and correlate this to their time in
        treatment media.
        
    
    Inputs:
        A list of strings with each element corresponding to the cell's phase
        at change
        
        A list of ints with each element corresponding to the cell's time 
        spent in the phase
        
        A list of lists containing how long each cell spends in the daughter
        cell Ss


    Outputs:
        Returning an n x 3 array, with each row corresponding to a cell
        column 1 is the phase of the cell at media change
        column 2 is frames into the phase the cell was before media change
        column 3 is how long the daughter S is 
        
    '''
    
    all_cell_S_stats = []
    
    for i in range(len(cell_phase_at_change)):
        
        phase_temp = cell_phase_at_change[i]
        time_temp = time_in_phase_at_change[i]
        
        if phase_temp == 'S':
            
            G1_temp = all_S_lengths[1]
            
        else:
            
            G1_temp = all_S_lengths[0]
            
        cell_temp = [phase_temp,time_temp_S_temp]
        
        all_cells_S_stats.append(cell_temp)
        

    return all_cells_S_stats


def get_cell_G2_stats(cell_phase_at_change, time_in_phase_at_change, all_G2_lengths):
        '''
    Purpose:
        To bin cells based on their fate and correlate this to their time in
        treatment media.
        
    
    Inputs:
        A list of strings with each element corresponding to the cell's phase
        at change
        
        A list of ints with each element corresponding to the cell's time 
        spent in the phase
        
        A list of lists containing how long each cell spends in the daughter
        cell G2s


    Outputs:
        Returning an n x 3 array, with each row corresponding to a cell
        column 1 is the phase of the cell at media change
        column 2 is frames into the phase the cell was before media change
        column 3 is how long the daughter G2 is 
        
    '''
    
    all_cell_G2_stats = []
    
    for i in range(len(cell_phase_at_change)):
        
        phase_temp = cell_phase_at_change[i]
        time_temp = time_in_phase_at_change[i]
        
        if phase_temp == 'G2':
            
            G1_temp = all_G2_lengths[1]
            
        else:
            
            G1_temp = all_G2_lengths[0]
            
        cell_temp = [phase_temp,time_temp_G2_temp]
        
        all_cells_G2_stats.append(cell_temp)
        

    return all_cells_G2_stats


if __name__ == '__main__':
    main()

