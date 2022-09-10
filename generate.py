#!/usr/bin/env python
# coding: utf-8

# In[15]:


from random import randint
import numpy as np
from collections import defaultdict
import pickle

with open('transitions.pkl', 'rb') as file:
    transitions = pickle.load(file)

def generate_using():
    i = randint(0, len(list(transitions.keys()))-1)
    current = list(transitions.keys())[i][1]
    pre = list(transitions.keys())[i][0]
    result = [current]
    n = int(input())
    for i in range(n-1):
        next_word = np.random.choice(transitions[(pre, current)])
        pre, current = current, next_word
        result.append(current)
    return " ".join(result)

generate_using()

