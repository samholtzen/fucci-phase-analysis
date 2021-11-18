import numpy
import utils


def main():

    all_data_str = numpy.loadtxt('for_project.csv', dtype=str, delimiter=',')
    # print(all_data_str)
    g1_lengths, s_lengths, g2_lengths = utils.count_phase_frames(all_data_str, 117)
    # print(g1_lengths)
    cell_phase_at_change, time_in_phase_at_change = utils.media_timing(all_data_str, 117)
    # print(time_in_phase_at_change)
    daughter_out_stats = utils.get_daughter_stats(cell_phase_at_change, time_in_phase_at_change,g1_lengths,s_lengths,g2_lengths)
    # print(daughter_out_stats)
    return None


if __name__ == '__main__':

    main()