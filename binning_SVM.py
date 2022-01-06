import numpy as np
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
import utils
import matplotlib.pyplot as plt
import csv
import pandas as pd

fig, ax = plt.subplots()

def make_meshgrid(ax, h=.02):
    # x_min, x_max = x.min() - 1, x.max() + 1
    # y_min, y_max = y.min() - 1, y.max() + 1
    x_min, x_max = ax.get_xlim()
    y_min, y_max = ax.get_ylim()

    xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                         np.arange(y_min, y_max, h))
    return xx, yy


def plot_contours(ax, clf, xx, yy, **params):
    Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)
    out = ax.contourf(xx, yy, Z, **params)
    return out


def draw_boundary(ax, clf):

    xx, yy = make_meshgrid(ax)
    return plot_contours(ax, clf, xx, yy,cmap=plt.cm.coolwarm, alpha=0.5)



# Read in files containing training data

cherry_training = utils.file_reader('training_data_cherry.csv')
venus_training = utils.file_reader('training_data_venus.csv')
fh = open('training_data_phase.csv')
phase_csv = csv.reader(fh)
phase_training = [row for row in phase_csv]


# Split the training data by mitoses and combine into three lists 1xn where
# n = number of data points

cherry_comb = []
venus_comb = []
phase_comb = []
for i in range(len(cherry_training)):
    mitoses = utils.mitosis_detection(venus_training[i])
    split_cherry, split_venus = utils.split_by_mitosis(cherry_training[i],
                                                       venus_training[i],
                                                       mitoses)
    _, split_phase = utils.split_by_mitosis(phase_training[i],
                                            phase_training[i],
                                            mitoses)

    for j in range(len(split_cherry)):
        cherry_comb.append(split_cherry[j])
        venus_comb.append(split_venus[j])
        phase_comb.append(split_phase[j])
flat_cherry = [item for sublist in cherry_comb for item in sublist]
flat_venus = [item for sublist in venus_comb for item in sublist]
flat_phase = [item for sublist in phase_comb for item in sublist]
flat_int = []

# Loop through and assign integer values for each phase_training 0=G1/G0, 1=S, 2=G1/M
for phase_training in flat_phase:

    if phase_training == 'G1':
        flat_int.append(0)

    elif phase_training == 'S':
        flat_int.append(1)

    elif phase_training == 'G2' or phase_training == 'M':
        flat_int.append(2)


# split our arrays into testing/training arrays
cherry_train, cherry_test, venus_train, venus_test, phase_train, phase_test = \
    train_test_split(flat_cherry, flat_venus, flat_int, random_state = 69)

# Zip up the testing and training floats to feed into the SVM
zip_train = list(zip(cherry_train,venus_train))
zip_test = list(zip(cherry_test,venus_test))

# initialize and fit the SVM using empirically defined C and gamma values

fucci_svm = SVC(C=6,
                kernel='rbf',
                gamma=9)
fucci_svm.fit(zip_train, phase_train)

# Plot the mCherry vs. mVenus values using the phases as the color
scatter = ax.scatter(cherry_train, venus_train, c=phase_train)
legend1 = ax.legend(*scatter.legend_elements(),
                    loc="upper right", title="Classes")
ax.add_artist(legend1)
plt.xlabel('mCherry Intensity (normalized)')
plt.ylabel('mCherry Intensity (normalized)')
plt.title('FUCCI Phase Assignment using Support Vector Machine')

# Draw boundaries using functions defined above
draw_boundary(ax, fucci_svm)

# Trying the model on actual data

cherry = utils.file_reader('mCherry_all_data.csv')
venus = utils.file_reader('mVenus_all_data.csv')

current_cherry = utils.normalize_signals(cherry[100])
current_venus = utils.normalize_signals(venus[100])

current_zip = list(zip(current_cherry, current_venus))
prediction = fucci_svm.predict(current_zip)

fig,ax = plt.subplots()

prediction = utils.assign_phase_to_frame(current_cherry,current_venus,prediction)


ax.scatter(range(len(current_cherry)), current_cherry)
ax.scatter(range(len(current_cherry)), prediction*0.2)

plt.show()

# convert predictions to strings
phases = []
for frame in prediction:
    if frame == 0:
        phases.append('G1')
    elif frame == 1:
        phases.append('S')
    elif frame == 2:
        phases.append('G2')
    elif frame == 4:
        phases.append('M')

