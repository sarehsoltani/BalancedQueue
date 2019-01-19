import random
from copy import deepcopy
import numpy as np

class Problem():
    def initialState(self):
       k = 2
       #queue= np.random.randint(1,10,3*k)
       queue = [2, 3, 6, 9, 7, 2]
       print(queue)

p = Problem()
p.initialState()