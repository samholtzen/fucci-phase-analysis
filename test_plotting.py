import utils
import plotly.graph_objects as go


mVenus = utils.file_reader('mVenus_all_data.csv')
mCherry = utils.file_reader('mCherry_all_data.csv')

mitoses = utils.mitosis_detection(mVenus[10])
print(mitoses)

split_cherry, split_venus = utils.split_by_mitosis(mCherry[10],mVenus[10])

fig = go.Figure()
frame_vec = [i for i in range(len(split_cherry[1]))]

fig.add_trace(go.Scatter(x=frame_vec,
                                 y=utils.normalize_signals(split_venus[1]),
                                 mode='lines',
                                 name=f'mVenus for Cell {1}',
                                 line=dict(color='rgba(153, 255, 51, .8)')))

fig.add_trace(go.Scatter(x=frame_vec,
                                 y=utils.normalize_signals(split_cherry[1]),
                                 mode='lines',
                                 name=f'mCherry for Cell {1}',
                                 line=dict(color='rgba(152, 0, 0, .8)')))

fig.show()
# utils.plotting_tracks(mVenus,mCherry,track_ids=[450,255,100],random_tracks=10)