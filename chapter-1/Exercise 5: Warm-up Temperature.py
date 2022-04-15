import random
import numpy as np

def accept_prob(S_old, S_new, T):
    # this is the acceptance "probability" in the greedy hill-climbing method
    # where new solutions are accepted if and only if they are better
    # than the old one.
    # change it to be the acceptance probability in simulated annealing
    if S_new > S_old:                         #simply return 1 if the new solution is better than the old one
        return 1                              #you dont really have to do this since you will return a value greater than 1 if the new solution is better, but the exercise required it
    else:                                     #if the new solution is worse, we should calculate a probability for it to be accepted
        return np.exp(-(S_old-S_new)/T)       #the probability algorithm


# the above function will be used as follows. this is shown just for
# your information; you don't have to change anything here
def accept(S_old, S_new, T):
    if random.random() < accept_prob(S_old, S_new, T):
        print(True)
    else:
        print(False)
