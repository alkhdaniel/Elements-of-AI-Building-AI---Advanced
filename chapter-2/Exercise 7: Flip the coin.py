import numpy as np

def generate(p1):
    # change this so that it generates 10000 random zeros and ones
    # where the probability of one is p1
    return np.random.choice([0,1], p=[1-p1, p1], size=10000)

def count(seq):
    result = 0
    i = 0
    for i in range(len(seq)-4):     #iterate through all numbers in the sequence except the last 4 (since they cant have 5 1's in a row)
        if seq[i:i+5].all():        #checks for a sequence of 5 1's in a row
            result+=1;              #add 1 to result
    return result

def main(p1):
    seq = generate(p1)
    return count(seq)

print(main(2/3))
