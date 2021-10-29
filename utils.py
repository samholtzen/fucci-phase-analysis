import csv
import sys
import numpy as np

'''
    utils provides definitions to take in file,
    turn it into a list of lists, __________
'''

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
            print(data)
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
    return derivative

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
        # Add list to main ratio list
    return ratio
    

#Testing Scripts
#print(file_reader("mCherry_sample_test.csv"))
#file_reader("mVenus_sample_test.csv")
#print(get_derivative([[1,2,3,4,5],[1,3,5,7,9],[1,4,7,10,13]]))
#print(get_ratio([[1,2,3,4,5],[1,1,1,1,1]],[[1,2,3,4,5],[0,1,2,3,4]]))
