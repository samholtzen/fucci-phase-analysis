import utils
import numpy as np
import random
import plotly.graph_objects as go

mVenus = utils.file_reader('mVenus_all_data.csv')
mCherry = utils.file_reader('mCherry_all_data.csv')

track = random.randint(0, len(mVenus))
print(track)

venus_norm = utils.normalize_signals(mVenus[track])
cherry_norm = utils.normalize_signals(mCherry[track])
mitoses = utils.mitosis_detection(mVenus[track])

phases = utils.assign_phase_to_frame(cherry_norm, venus_norm)

print(phases)
ph_num_clean = []

for frame in phases:
    if frame == 'G1':
        ph_num_clean.append(0.2)
    elif frame == 'S':
        ph_num_clean.append(0.4)
    elif frame == 'G2':
        ph_num_clean.append(0.6)
    elif frame == 'M':
        ph_num_clean.append(1)

kernel_size = 10
kernel = np.ones(kernel_size) / kernel_size

venus_norm_conv = np.convolve(venus_norm, kernel, mode='same')
cherry_norm_conv = np.convolve(cherry_norm, kernel, mode='same')

venus_at_mitosis = [venus_norm_conv[mitosis] for mitosis in mitoses]
venus_diff_conv = np.diff(venus_norm_conv)

frames = [i for i in range(len(venus_norm))]

fig = go.Figure()
fig.add_trace(go.Scatter(x=frames,
                         y=venus_norm,
                         mode='lines',
                         name='normalized mVenus'))

fig.add_trace(go.Scatter(x=mitoses,
                         y=venus_at_mitosis,
                         mode='markers',
                         name='Mitoses'))

fig.add_trace(go.Scatter(x=frames,
                         y=cherry_norm,
                         mode='lines',
                         name='normalized mCherry'))

fig.add_trace(go.Scatter(x=frames,
                         y=ph_num_clean,
                         mode='markers',
                         name='clean'))

fig.show()
