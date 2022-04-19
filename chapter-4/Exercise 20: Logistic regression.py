import math
import numpy as np

x = np.array([4, 3, 0])
c1 = np.array([-.5, .1, .08])
c2 = np.array([-.2, .2, .31])
c3 = np.array([.5, -.1, 2.53])

def sigmoid(x):
	return 1 / (1 + math.exp(-x))

# calculate the output of the sigmoid for x with all three coefficients
print (sigmoid(x[0]*c1[0]+x[1]*c1[1]+x[2]*c1[2]))
print (sigmoid(x[0]*c2[0]+x[1]*c2[1]+x[2]*c2[2]))
print (sigmoid(x[0]*c3[0]+x[1]*c3[1]+x[2]*c3[2]))
