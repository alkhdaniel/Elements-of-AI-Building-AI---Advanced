import numpy as np
from io import StringIO

input_string = '''
25 2 50 1 500 127900
39 3 10 1 1000 222100
13 2 13 1 1000 143750
82 5 20 2 120 268000
130 6 10 2 600 460700
115 6 10 1 550 407000
'''

np.set_printoptions(precision=1)    # this just changes the output settings for easier reading
 
def fit_model(input_file):
    # Please write your code inside this function
    data = np.genfromtxt(input_file, skip_header=1)   #generate 2d array from the data
    x = data[:,:-1]                                   #put all dependent variables in x (all but the last column in our dataset)
    y = data[:,-1]                                    #put all independent variables in y (the last column in our dataset)
    c = np.linalg.lstsq(x, y)[0]                      #find the least squares
    print(c)                                          #output the coefficients given from the least squares
    print(x @ c)                                      #output the dependent variable given our new coefficients


# simulate reading a file
input_file = StringIO(input_string)
fit_model(input_file)
