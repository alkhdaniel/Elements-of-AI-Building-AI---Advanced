import numpy as np

# data
X = np.array([[66, 5, 15, 2, 500], 
              [21, 3, 50, 1, 100], 
              [120, 15, 5, 2, 1200]])
y = np.array([250000, 60000, 525000])

# alternative sets of coefficient values
c = np.array([[3000, 200 , -50, 5000, 100], 
              [2000, -250, -100, 150, 250], 
              [3000, -100, -150, 0, 150]])   

def find_best(X, y, c):
    smallest_error = np.Inf
    best_index = -1
    for coeff in c:
        predicted = (X @ coeff)                         #get the predicted price when using the alternative sets of coefficient values
        for i in range(len(predicted)):                 #iterate through the predicted prices so we can compare them to the actual values
            least_square = ((y[i]-predicted[i])**2)     #get the squares (actual value - predicted value)^2
            if least_square < smallest_error:           #if the squares are smaller than our best model, we save it
                best_index = i                          
                smallest_error = least_square
    print("the best set is set %d" % best_index)


find_best(X, y, c)
