import utils
import random

mVenus = utils.file_reader('mVenus_all_data.csv')
mCherry = utils.file_reader('mCherry_all_data.csv')


track = random.randint(0, len(mVenus))

venus_norm = utils.normalize_signals(mVenus[track])
cherry_norm = utils.normalize_signals(mCherry[track])
mitoses = utils.mitosis_detection(mVenus[track])

phases = utils.assign_phase_to_frame(venus_norm,cherry_norm)

phases_split, _ = utils.split_by_mitosis(phases,phases,mitoses)

print(phases_split)

