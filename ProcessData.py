import utils as ut
import normalize_utils


def main():
    """
This function runs main arguments.

Parameters
---------
a : str
First argument is the filename/path to mCherry file
B : str
Second argument is the filename/path to mVenus file
"""

    # Call input_parser to parse commandline inputs
    args = ut.input_parser()

    # Get data from file using file_reader
    mCherrydata = ut.file_reader(args.mCherryfilename)
    #print(len(mCherrydata))

    # Get data from file using file_reader
    mVenusdata = ut.file_reader(args.mVenusfilename)
    #print(len(mVenusdata))

    normalize_utils.find_mitosis_event(mCherrydata, mVenusdata)

    #Find derivative (rate of change) for each cell line
    mCherryDerivative = ut.get_derivative(mCherrydata)
    mVenusDerivative = ut.get_derivative(mVenusdata)

    #Find ratio between mCherry and mVenus for each cell line
    CherryToVenusRatio = ut.get_ratio(mCherrydata, mVenusdata)

    #Get the media_change frame from the input
    media_frame = args.mediaframe







if __name__ == '__main__':
    main()

