import numpy as np

x_train = np.random.rand(10, 3)   # generate 10 random vectors of dimension 3
x_test = np.random.rand(3)        # generate one more random vector of the same dimension

def dist(a, b):
    sum = 0
    for ai, bi in zip(a, b):
        sum = sum + (ai - bi)**2
    return np.sqrt(sum)
    
def nearest(x_train, x_test):
    nearest = -1
    min_distance = np.Inf
    # add a loop here that goes through all the vectors in x_train and finds the one that
    # is nearest to x_test. return the index (between 0, ..., len(x_train)-1) of the nearest
    # neighbor
    for index, cabin in enumerate(x_train):         #we need access to both the index and the cabin so we enumerate
        if dist(cabin, x_test) < min_distance:      #check if the distance between the current cabin and the test cabin is nearer than our nearest solution
            min_distance = dist(cabin, x_test)      #if it is; we save the min distance and the index
            nearest = index
    print(nearest)

nearest(x_train, x_test)
