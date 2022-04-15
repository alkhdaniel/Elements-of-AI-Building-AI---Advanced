portnames = ["PAN", "AMS", "CAS", "NYC", "HEL"]
 
def permutations(route, ports):
    # Write your recursive code here
    if len(ports) > 0:                                                  #checks if there are any ports left
        for i in range(len(ports)):                                     #loop through the remaining ports
            permutations(route+[ports[i]],ports[:i]+ports[i+1:])        #add one of each of the ports to the route and recursively run the function with that port removed from ports

    # Print the port names in route when the recursion terminates
    else:
        print(' '.join([portnames[i] for i in route]))                  #prints the line with all port names when there are no remaining ports


# This will start the recursion with 0 ("PAN") as the first stop
permutations([0], list(range(1, len(portnames))))
