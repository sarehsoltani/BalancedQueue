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
	
	#hueristic function that calculate the max of subarrays
    def FindMax(self,queue):
       tmp = [] 
       queue= split_list(queue, 2)
       #print(queue) 
       #print(sum(tem)) 
       for item in queue:   
        tmp.append(sum(item))
       #print(max(tmp))
       maxium = max(tmp) 
       return maxium 
	   
    def actions(self,state):
        results = []
        for i in range(0,6):
            for j  in range(i+1, 6):
                next_state = deepcopy(state)
                temp = next_state[i]
                next_state[i] = next_state[j]
                next_state[j] = temp
                value = self.FindMax(next_state)
                results.append(next_state)
                print(next_state,value)    
        return results
		
p = Problem()
#p.initialState()
#p.FindMax(p.initialState())
#p.actions(p.initialState())
hc = HillClimbing(p, 'random_restart')		

