import numpy as np
import matplotlib.pyplot as plt

# possible arguments
filePath = 'Fe3CReflexions.txt'
idxX = 4
idxY = 6

# data reading and metadata creation
data = np.loadtxt(open(filePath, encoding='ISO-8859-1').readlines()[:-2], skiprows=9, converters={6:lambda x: float(x[:-1])})
with open(filePath, encoding='ISO-8859-1') as fIn:
    for i in range(7):
        fIn.readline()
    headline = fIn.readline().split()
metadata = {'num. data points': data.shape[0], 'peak location': data[:,4][data[:,6].argmax()], 'colums':headline }

# output for development
print('Metadata:', metadata)

plt.plot(data[:,idxX], data[:,idxY])
plt.xlabel(headline[idxX])
plt.ylabel(headline[idxY])
plt.show()