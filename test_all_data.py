import utils
import numpy as np
import pandas as pd
import plotly.graph_objects as go

mVenus = utils.file_reader('mVenus_all_data.csv')
mCherry = utils.file_reader('mCherry_all_data.csv')

all_phases = []

for track in range(0, len(mVenus)):

    venus_norm = utils.normalize_signals(mVenus[track])
    cherry_norm = utils.normalize_signals(mCherry[track])
    mitoses = utils.mitosis_detection(mVenus[track])

    phases = utils.assign_phase_to_frame(cherry_norm, venus_norm)

    all_phases.append(phases)

all_phase_array = np.array(all_phases)

all_phase_compos = []
row_labels = []

for column in range(0, len(mCherry[0])):
    phase_compos = []
    data_slice = all_phase_array[:, column]
    slice_str = ''.join(data_slice)

    row_labels.append(column/5)
    phase_compos.append(slice_str.count('G1') / len(data_slice))
    phase_compos.append(slice_str.count('S') / len(data_slice))
    phase_compos.append(slice_str.count('G2') / len(data_slice))
    phase_compos.append(slice_str.count('M') / len(data_slice))

    all_phase_compos.append(phase_compos)

phase_df = pd.DataFrame(data=all_phase_compos, columns=['G1', 'S', 'G2', 'M'], index=row_labels)

time = phase_df.index

fig = go.Figure()
fig.add_bar(x=time, y=phase_df.G1, name='Fraction of Cells in G1')
fig.add_bar(x=time, y=phase_df.S, name='Fraction of Cells in S')
fig.add_bar(x=time, y=phase_df.G2, name='Fraction of Cells in G2')
fig.add_bar(x=time, y=phase_df.M, name='Fraction of Cells in M')
fig.update_layout(barmode="stack",
                  title="Cell Cycle Phase Distribution Over Time",
                  xaxis_title='Time (h)',
                  yaxis_title='Fraction of Cells')
fig.show()
