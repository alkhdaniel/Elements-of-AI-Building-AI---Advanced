portnames = ["PAN", "AMS", "CAS", "NYC", "HEL"]

# https://sea-distances.org/
# nautical miles converted to km

D = [
        [0,8943,8019,3652,10545],
        [8943,0,2619,6317,2078],
        [8019,2619,0,5836,4939],
        [3652,6317,5836,0,7825],
        [10545,2078,4939,7825,0]
    ]

# https://timeforchange.org/co2-emissions-shipping-goods
# assume 20g per km per metric ton (of pineapples)

co2 = 0.020

# DATA BLOCK ENDS

# these variables are initialised to nonsensical values
# your program should determine the correct values for them
smallest = 1000000
bestroute = [0, 0, 0, 0, 0]

def permutations(route, ports):
    global smallest, bestroute
    # write the recursive function here
    # remember to calculate the emissions of the route as the recursion ends
    # and keep track of the route with the lowest emissions
    if len(ports) > 0:                                                  #checks if there are any ports left
        for i in range(len(ports)):                                     #loop through the remaining ports
            permutations(route+[ports[i]],ports[:i]+ports[i+1:])        #add one of each of the ports to the route and recursively run the function with that port removed from ports
    else:
        routeemission = 0;
        for i in range(len(route)-1):                                   #iterates between ports and adds the route emissions between all of them together
             routeemission += D[route[i]][route[i+1]]*co2
        if routeemission < smallest:                                    #save the route if the emissions are lower than our current best route
            smallest = routeemission
            bestroute = route

def main():
    # Do not edit any (global) variables using this function, as it will mess up the testing

    # this will start the recursion 
    permutations([0], list(range(1, len(portnames))))

    # print the best route and its emissions
    print(' '.join([portnames[i] for i in bestroute]) + " %.1f kg" % smallest)

main()
