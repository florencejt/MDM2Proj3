import numpy as np
import matplotlib.pyplot as plt


n_0 = 0
k2 = 150 #  rate of people arriving
k1 = 60/47   # rate of people leaving

timeVec = []
AVec = []
counter = 0
numrealisations = 10
fig1 = plt.figure()
totalVec = []
totalTimeVec = []
for i in range(numrealisations):
    timeVec = []
    AVec = []
    A = n_0
    AVec.append(A)
    t = 0
    timeVec.append(t)
    counter = counter + 1
    while t < 24:
        r1 = np.random.uniform(0, 1, None)
        r2 = np.random.uniform(0, 1, None)
        alpha = (A*k1) + k2
        t = t + (1/alpha)*np.log(1/r1)
        timeVec.append(t)
        counter = counter + 1
        if r2 < (k2/alpha):
            A = A + 1
            AVec.append(A)
        else:
            A = A - 1
            AVec.append(A)
    totalVec.append(AVec)
    totalTimeVec.append(timeVec)
    plt.step(timeVec, AVec,linewidth=0.5)

counter = len(min(totalVec,key=len))
finalTimeVec = min(totalTimeVec,key=len)
meanValuesVec = []

for j in range(counter):
    meanValue = (totalVec[0][j]+totalVec[1][j]+totalVec[2][j])/3
    meanValuesVec.append(meanValue)

plt.plot(finalTimeVec, meanValuesVec,c='k')
plt.title('Constant Arrival Rate k2={}'.format(k2))
plt.xlabel('Time (hours)')
plt.ylabel('Number of car park spaces taken')
plt.xlim(0,24)
plt.show()