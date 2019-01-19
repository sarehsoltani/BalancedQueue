from SearchAlgorithms.HillClimbing import *
import random
from copy import deepcopy
import numpy as np

def split_list(alist, wanted_parts):
    length = len(alist)
    return [ alist[i*length // wanted_parts: (i+1)*length // wanted_parts] for i in range(wanted_parts) ]

class Problem():
    def initialState(self):
       k = 2
       #queue= np.random.randint(1,10,6)
       queue = [2, 8, 6, 5, 2, 0]
       #print(queue)
       return queue

p = Problem()
p.initialState()