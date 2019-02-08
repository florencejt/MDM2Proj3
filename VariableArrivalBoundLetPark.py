import numpy as np
import matplotlib.pyplot as plt

def arrivalrate(t):
    return(30 * np.sin((t / 2) + 5) - 30* np.sin(t / 3))


n_0 = 0
k2init = 150 #rate of people arriving
k1 = 60/47   #rate of people leaving
overfill = 0
boundary = 165
timeVec = []
AVec = []
totalTimeVec = []
totalVec=[]
numrealisations = 100
for i in range(numrealisations):
    k2 = k2init
    k1 = 60 / 47
    timeVec = []
    AVec = []
    A = n_0
    AVec.append(A)
    t = 0
    timeVec.append(t)
    r1 = np.random.uniform(0, 1, None)
    r2 = np.random.uniform(0, 1, None)
    alpha = (A*k1) + k2
    t = t + (1/alpha)*np.log(1/r1)
    timeVec.append(t)
    if r2 < (k2/alpha):
        A = A + 1
        AVec.append(A)
    else:
        A = A - 1
        AVec.append(A)
    k2 = arrivalrate(t)+k2init
    if A > boundary:
        overfill = overfill + 1
    while t < 24:
        r1 = np.random.uniform(0, 1, None)
        r2 = np.random.uniform(0, 1, None)
        k2 = arrivalrate(t) + k2init
        alpha = (A*k1) + k2
        t = t + (1/alpha)*np.log(1/r1)
        timeVec.append(t)
        if r2 < (k2/alpha):
            A = A + 1
            AVec.append(A)
        else:
            A = A - 1
            AVec.append(A)
        if A > boundary:
            overfill = overfill + 1
    totalVec.append(AVec)
    totalTimeVec.append(timeVec)
    plt.step(timeVec, AVec, linewidth=0.5)

counter = len(min(totalVec,key=len))
finalTimeVec = min(totalTimeVec,key=len)
meanValuesVec = []

for j in range(counter):
    meanValue = (totalVec[0][j]+totalVec[1][j]+totalVec[2][j])/3
    meanValuesVec.append(meanValue)

plt.plot(finalTimeVec, meanValuesVec,c='k')
ratio = (((overfill/numrealisations))/len(finalTimeVec))*100
print('probability that all car park spaces are taken = {} %'.format(ratio))

plt.plot(finalTimeVec,[boundary]*len(finalTimeVec),c='r')
plt.title('Arrival rate based on sine curve with arrival rate k2={}'.format(k2init))
plt.xlabel('Time (hours)')
plt.ylabel('Number of car park spaces taken')
plt.xlim(0,24)
# mean
# meanLine = (1/math.factorial(counterVec))*((k2/k1)**counterVec)*np.exp(-k2/k1)

plt.show()
