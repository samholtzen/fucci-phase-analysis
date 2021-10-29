'''
    defines function to enter filename and column
    number and return unquie values in column
    and counts of each.
'''

import utils as ut
import argparse as argp
import configparser as conp


def main():
    '''
    This function runs main arguments.

    Parameters
    —---------
    a : str
    First argument is the filename/path to mCherry file
    B : str
    Second argument is the filename/path to mVenus file
    '''

    # Call input_parser to parse commandline inputs
    args = input_parser()
    # Get data from file using file_reader
    mCherrydata = ut.file_reader(args.mCherryfilename)
    # Get data from file using file_reader
    mVenusdata = ut.file_reader(args.mVenusfilename)
    #Find derivative (rate of change) for each cell line
    mCherryDerivative = ut.get_derivative(mCherrydata)
    mVenusDerivative = ut.get_derivative(mVenusdata)
    #Find ratio between mCherry and mVenus for each cell line
    CherryToVenusRatio = ut.get_ratio(mCherrydata, mVenusdata)
    
    #Testing Scripts
    print(mCherryDerivative)
    print(mVenusDerivative)
    print(CherryToVenusRatio)
    
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
    counter_inputs = parser.parse_args()
    # Exception Handling of input errors
    if (counter_inputs.mVenusfilename and counter_inputs.mCherryfilename):
        allcommands = True
        anycommands = True
    elif (counter_inputs.mVenusfilename or counter_inputs.mCherryfilename):
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
    # use config file instead
    elif counter_inputs.configfile:
        if anycommands is False:
            config = conp.ConfigParser()
            config.read(counter_inputs.configfile[0])
            # read in mCherry filename
            counter_inputs.mCherryfilename = config['FILES']['mCherry']
            # read in mVenus filename
            counter_inputs.mVenusfilename = config['FILES']['mVenus']
        else:
            # Check for which value(s) were extras
            if counter_inputs.mCherryfilename:
                raise AttributeError('Both a config file and mCherry filename \
                were entered')
            if counter_inputs.mVenusfilename:
                raise AttributeError('Both a config file and mVenus filename \
                were entered')
    return counter_inputs


if __name__ == '__main__':
    main()


# Testing Scripts
# main()
# print(input_parser())