import numpy as np
import matplotlib.pyplot as plt


n_0 = 20
k = 0.1
dt = 0.005

timeVec = []
AVec = []

A = n_0
AVec.append(A)
t = 0
timeVec.append(t)
numrealisations = 10
fig1 = plt.figure()
for i in range(numrealisations):
    timeVec = []
    AVec = []
    A = n_0
    AVec.append(A)
    t = 0
    timeVec.append(t)
    while A > 0:
        r = np.random.uniform(0, 1, None)
        t = t + dt
        if r < (A * k * dt):
            A = A - 1
            AVec.append(A)
            timeVec.append(t)
        else:
            A = A
            AVec.append(A)
            timeVec.append(t)
    plt.step(timeVec, AVec)

meanVec =[];
for i in range(len(timeVec)):
    meaneq = n_0 * np.exp(-k*timeVec[i])
    meanVec.append(meaneq)

plt.step(timeVec,meanVec,c='k',linewidth=2)
plt.show()