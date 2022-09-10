#!/usr/bin/env python
# coding: utf-8

# In[2]:


from collections import defaultdict
import re
import pickle

with open('The_Master_and_Margarita.txt', encoding = 'windows-1251') as f:
    text = f.read()
text_2 = re.sub(r'([^а-я]+)', ' ', text.lower().replace('\n', ' '))
document = [i for i in text_2.split()]
transitions = defaultdict(list)
for pre, current, next in zip(document, document[1:], document[2:]):
    transitions[(pre, current)].append(next)

with open('transitions.pkl', 'wb') as file:
    pickle.dump(transitions, file)


# In[ ]:




