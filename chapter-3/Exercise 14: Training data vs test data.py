import numpy as np
from io import StringIO


train_string = '''
25 2 50 1 500 127900
39 3 10 1 1000 222100
13 2 13 1 1000 143750
82 5 20 2 120 268000
130 6 10 2 600 460700
115 6 10 1 550 407000
'''

test_string = '''
36 3 15 1 850 196000
75 5 18 2 540 290000
'''

def main():
    np.set_printoptions(precision=1)    # this just changes the output settings for easier reading
    
    # Please write your code inside this function
    traindata = np.genfromtxt(StringIO(train_string), skip_header=1)  #read the training data
    testdata = np.genfromtxt(StringIO(test_string), skip_header=1)    #read the testing data
    train_x = traindata[:,:-1]                                        #save the independent variables in the train data to train_x
    train_y = traindata[:,-1]                                         #save the dependent variable in the train data to train_y
    test_x = testdata[:,:-1]                                          #save the independent variables in the test data to test_x
    test_y = testdata[:,-1]                                           #save the dependent variable in the test data to test_y
    c = np.linalg.lstsq(train_x, train_y)[0]                          #get least square coefficients from the test data
    print(c)                                                          #print the coefficients
    print(test_x @ c)                                                 #apply the coefficients to the test data and print it


main()
