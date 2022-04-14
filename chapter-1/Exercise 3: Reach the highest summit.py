import math
import random             	# just for generating random mountains                                 	 

# generate random mountains                                                                               	 

w = [.05, random.random()/3, random.random()/3]
h = [1.+math.sin(1+x/.6)*w[0]+math.sin(-.3+x/9.)*w[1]+math.sin(-.2+x/30.)*w[2] for x in range(100)]

def climb(x, h):
    # keep climbing until we've found a summit
    summit = False

    # edit here
    while not summit:
        summit = True                                             #set summit to true even if it isnt yet; we will set this back to false if a new summit is found
        for x_new in range(max(0, x-5), min(99, x+5)):            #check all positions from 5 steps to the left to 5 steps to the right
            if h[x_new] > h[x]:                                   #if a new peak was found
                x=x_new                                           #replace the old position with the new one
                summit = False                                    #set summit to false to continue searching if there are even higher peaks
    return x


def main(h):
    # start at a random place                                                                                  	 
    x0 = random.randint(1, 98)
    x = climb(x0, h)

    return x0, x

main(h)
