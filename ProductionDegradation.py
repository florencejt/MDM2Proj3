import numpy as np
import matplotlib.pyplot as plt
import math
# how to make the lines straight
# adding in the mean line

n_0 = 0
k1 = 0.1 # rate of people leaving?
k2 = 1 # rate of people arriving

timeVec = []
AVec = []

A = n_0
AVec.append(A)
t = 0
timeVec.append(t)
numrealisations = 5
numsteps = 100
fig1 = plt.figure()
for i in range(numrealisations):
    timeVec = []
    AVec = []
    A = n_0
    AVec.append(A)
    t = 0
    timeVec.append(t)
    for k in range(numsteps):
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
    plt.step(timeVec, AVec)

# meanVec =[];
# phi_0 = 0
# meanVec.append(phi_0)
# phi_n = (k2/k1)*phi_0
# meanVec.append(phi_n)
# for i in range(len(timeVec)-2):
#     phi_n+1 = (1/k1*(n+1))*(k1*n*)
# for i in range(len(timeVec)):
#     meaneq = (1/math.factorial(numsteps))
#     meanVec.append(meaneq)

#meaneq = (n)

plt.show()