#Didnt find an elegant solution to this problem, i doubt the way im doing it here is optimal. Might revisit it in the future.
import numpy as np
data = [[1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1],
        [1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 0, 1, 3, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1]]
def find_nearest_pair(data):
    N = len(data)
    dist = np.empty((N, N), dtype=np.float)
    for i in range(N):
        for j in range(N):
            if(i==j):
                dist[i][j] = np.inf                             #set distance to infinite if we are comparing the same element
            else:
                dist[i][j]=0                                    #set the distance to 0 because we will be adding to it
                for x in range(len(data[i])):
                    dist[i][j] += abs(data[i][x]-data[j][x])    #add the absolute difference between i and j
    print(np.unravel_index(np.argmin(dist), dist.shape))
find_nearest_pair(data)
