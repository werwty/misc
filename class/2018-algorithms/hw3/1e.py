#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sys
import math


# In[62]:


input1 = input()
input2 = input()
value, num_denom = [int(n) for n in input1.split()] #sys.argv[1].split()
input2_values = [int(n) for n in input2.split()]#sys.argv[2].split()

denominations = sorted(input2_values, reverse=True)


# In[77]:


def makeChange(denoms, value):
    import ipdb; ipdb.set_trace()
    # initialize array with infinity for all values
    dynamic_array = [float("inf") for i in range(0, value+1)]
    # except for the first value, 0.
    dynamic_array[0] = 0
    

    for i in range(1, value+1):
        for j in range(0, len(denoms)):
            if (denoms[j] <= i):
                a = dynamic_array[i-denoms[j]]
                if a < float("inf") and a + 1 < dynamic_array[i]:
                    dynamic_array[i]= a + 1
               
    return dynamic_array[value]; 


# In[78]:


print(makeChange(denominations, value))


# In[ ]:




