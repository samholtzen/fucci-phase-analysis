import csv
import sys
import numpy as np
import matplotlib as mp
import pandas as pd

'''
    utils provides definitions to take in file,
    turn it into a list of lists, determine phases
    and conduct calculations on the phases to export
    for plotting.
'''



def input_parser():
    '''
    This function processes/parses commandline
    arguments and input parsed files.
    '''
    parser = argp.ArgumentParser(description="Counter Function")
    # input argument ‘c’ is configfile (string)
    
    parser.add_argument(
        '-c', '--configfile',
        type=str,
        nargs=1,
        action='store',
        required=False,
        help='This is a optional configfile')
    
    # input argument ‘a’ is mCherry filename (string)
    parser.add_argument(
        '-a', '--mCherryfilename',
        type=str,
        action='store',
        required=False,
        help='This string here is the mCherry data filename')
    
    # input argument ‘b’ is mVenus filename (string)
    parser.add_argument(
        '-b', '--mVenusfilename',
        type=str,
        action='store',
        required=False,
        help='This string here is the mVenus data filename')
    
    parser.add_argument(
        '-t', '--mediaframe',
        type=int,
        action='store',
        required=False,
        help='The frame at which the media was changed goes here')
    
    counter_inputs = parser.parse_args()
    # Exception Handling of input errors
    if (counter_inputs.mVenusfilename and counter_inputs.mCherryfilename
       and counterinputs.mediaframe):
        allcommands = True
        anycommands = True
    elif (counter_inputs.mVenusfilename or counter_inputs.mCherryfilename
         or counter_inputs.mediaframe):
        allcommands = False
        anycommands = True
    else:
        anycommands = False
    # use command args if no config file but do have command args
    if counter_inputs.configfile is None:
        if allcommands:
            # convert parse arg ints from lists back into ints
            a = 1
        else:
            # Check for which value(s) is/are missing
            if counter_inputs.mCherryfilename is None:
                raise AttributeError('There is no value for mCherry filename or \
                config file')
            if counter_inputs.mVenusfilename is None:
                raise AttributeError('There is no value for mVenus filename or \
                config file')
            if counter_inputs.mediaframe is None:
                raise AttributeError('There is no value for media frame or \
                config file')
    # use config file instead
    elif counter_inputs.configfile:
        if anycommands is False:
            config = conp.ConfigParser()
            config.read(counter_inputs.configfile[0])
            # read in mCherry filename
            counter_inputs.mCherryfilename = config['FILES']['mCherry']
            # read in mVenus filename
            counter_inputs.mVenusfilename = config['FILES']['mVenus']
            # read in the media change frame
            counter_inputs.mediaframe = config['PARAMETERS']['media_chage_frame']
        else:
            # Check for which value(s) were extras
            if counter_inputs.mCherryfilename:
                raise AttributeError('Both a config file and mCherry filename \
                were entered')
            if counter_inputs.mVenusfilename:
                raise AttributeError('Both a config file and mVenus filename \
                were entered')
            if counter_inputs.mediaframe:
                raise AttributeError('Both a config file and media change frame \
                were entered')
    return counter_inputs



def file_reader(filename, delimiter=' '):
    '''
    Returns list of each line made up of lists of values.

            Parameters:
                    filename (filepath): File path of file
                    delimiier (string): String to sperate values within line

            Returns:
                    data_list(list of lists): List of values within each line.
    '''
    # Exception Handling for opening invalid file
    try:
        # Open filename using open method
        with open(filename, newline='') as f_input:
            data = [list(map(float, row)) for row in csv.reader(f_input)]
            # print(data)
    except FileNotFoundError:
        print('FileNotFoundError: file "%s" does not exist.' % filename, file=sys.stderr)
        # Exit code 1
        sys.exit(1)
    return data

def get_derivative(data):
    '''
    Returns list of each line made up of lists of values.

            Parameters:
                    data(list of lists): list of floirent values in cell line.

            Returns:
                    dervivative(list of arrays): Derivatives at each point in each cell line. 
    '''
    # Initialize
    derivative = []
    # loop through all cell lines
    for line in data:
        cellLineDiff = np.diff(line,1)
        derivative.append(cellLineDiff)
    derivativeArray=np.array([np.array(xi) for xi in derivative])
    return derivativeArray

def get_ratio(cherry, venus):
    '''
    Returns list of each line made up of lists of values.

            Parameters:
                    cherry(list of lists): list of floirent values in cell line.
                    venus(list of lists): list of floirent values in cell line.

            Returns:
                    ratio(list of lists): List of ratios for each cell line.
    '''
    # Initialize
    ratio = venus
    # loop through all cell lines
    for line in range(len(venus)):
        # Loop through each point in the cell lines
        for point in range(len(venus[1])):
            c = cherry[line][point]
            v = venus[line][point]
            # Take ratio of Cherry to Venus
            # Check that v is not zero
            if v == 0:
                # if v is 0, return it to very small value
                v = .00000001
            pointRatio = c/v
            # Add ratio value to main data file
            ratio[line][point] = pointRatio
    ratioArray=np.array([np.array(xi) for xi in ratio])
    return ratioArray
    
    
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
        cellstr_temp = ''.join(cell)

        # Only look at cells after the media change
        cellstr_temp = cellstr_temp[media_frame:]
        
        # Split the array into individual cell traces by split string at 'M'
        cell_split = cellstr_temp.split('M')
        
        G1_lengths = []
        S_lengths = []
        G2_lengths = []
        
        for i in range(len(cell_split)):
            
            # Loop through and find the number of instances of "G1"
            G1_length = cell_split[i].count('G1')
            G1_lengths.append(G1_length/5)
            
            # Same for S and G2
            S_length = cell_split[i].count('S')
            S_lengths.append(S_length/5)
            
            G2_length = cell_split[i].count('G2')
            G2_lengths.append(G2_length/5)
        
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
        phase_before = phase_at_change
        
        while phase_before == phase_at_change:
            
            if frame_to_check > 2:
                
                phase_before = cell[frame_to_check]
                time_in_phase += 1
                frame_to_check -= 1
                
            else:
                
                break
        
        time_in_phase_at_change.append(time_in_phase/5)
    
    return cell_phase_at_change, time_in_phase_at_change


def get_daughter_stats(cell_phase_at_change, time_in_phase_at_change, all_G1_lengths, all_G2_lengths, all_S_lengths):
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
        colum 4 is how long the daughter S is
        column 5 is how long the daughter G2 is
        
    '''
    
    daughter_cell_stats = []
    
    for i in range(len(cell_phase_at_change)):
        
        phase_temp = cell_phase_at_change[i]
        time_temp = time_in_phase_at_change[i]
        
        if phase_temp == 'G1':
            
            S_temp = all_S_lengths[0]
            G2_temp = all_G2_lengths[0]
            
            if len(all_G1_lengths) > 1:
                G1_temp = all_G1_lengths[1]
            else:
                G1_temp = all_G1_lengths[0]
                    
            
        elif phase_temp == 'S':
            
            G1_temp = all_G1_lengths[0]
            G2_temp = all_G2_lengths[0]
            
            if len(all_S_lengths) > 1:
                S_temp = all_S_lengths[1]
            else:
                S_temp = all_S_lengths[0]
            
        elif phase_temp == 'G2':
            
            G1_temp = all_G1_lengths[0]
            S_temp = all_S_lengths[0]
            
            if len(all_G2_lengths) > 1:
                G2_temp = all_G2_lengths[1]
            else:
                G2_temp = all_G2_lengths[0]            
            
        cell_temp = [phase_temp,time_temp,G1_temp,S_temp,G2_temp]
        
        daughter_cell_stats.append(cell_temp)
        
    return daughter_cell_stats

def convert_phase_to_time(daughter_cell_stats):
    '''
    Purpose:
        To convert Phase and Time into Phase into a pseudotime for plotting
        
    
    Inputs:
        All of the cell stats, which houses the phase, the 


    Outputs:
        Returning an n x 4 array, with each row corresponding to a cell
        column 1 is the time into the cell cycle a cell is at
        the time of media change
        
        column 2 is how long the daughter G1 is 
        column 3 is how long the daughter S is
        column 4 is how long the daughter G2 is
    '''
    
    daughter_cell_to_plot = []
    
    for daughters in all_cell_stats:
        
        phase = daughters[0]
        time = daughters[1]
        lengths = daughters[2:]
        
        if phase == 'G1':
            phase_out = time
        elif phase == 'S':
            phase_out = time + 4
        elif phase == 'G2':
            phase_out = time + 9
        
        time_convert_temp = [phase_out,lengths]
        
        daughter_cell_to_plot.append(time_convert_temp)
        
            
    return daughter_cell_to_plot


def write_list_csv(daughter_cell_stats):
    
    daughter_cell_stats_df = pd.DataFrame(daughter_cell_stats,
                                          columns=['Phase','Time',
                                                   'Daughter_G1','Daughter_S',
                                                   'Daughter_G2'])
    
    daughter_cell_stats_df.to_csv('daughter_cell_phases.csv',index=False, header=True)
    
    
    return None


#Testing Scripts
#print(file_reader("mCherry_sample_test.csv"))
#file_reader("mVenus_sample_test.csv")
#print(get_derivative([[1,2,3,4,5],[1,3,5,7,9],[1,4,7,10,13]]))
#print(get_ratio([[1,2,3,4,5],[1,1,1,1,1]],[[1,2,3,4,5],[0,1,2,3,4]]))
