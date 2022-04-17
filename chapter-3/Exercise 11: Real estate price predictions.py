# input values for three mökkis: size, size of sauna, distance to water, number of indoor bathrooms, 
# proximity of neighbors
X = [[66, 5, 15, 2, 500], 
     [21, 3, 50, 1, 100], 
     [120, 15, 5, 2, 1200]]
c = [3000, 200, -50, 5000, 100]    # coefficient values

def predict(X, c):
    for cabin in X:                       #iterate cabins
        price = 0                         #set price to 0 because we will add to it soon
        for i in range(len(c)):           #iterate through all coefficients
            price += cabin[i]*c[i]        #add coefficient*predictor to the price until we run out of coefficients
        print(price)

predict(X, c)
