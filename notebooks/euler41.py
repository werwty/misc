#!/usr/bin/env python
# coding: utf-8

# In[3]:


def Esieve(limit):
    a = [True] * limit
    a[0] = a[1] = False

    for (i, isprime) in enumerate(a):
        if isprime:
            yield i
            for n in xrange(i*i, limit, i):     # Mark factors non-prime
                a[n] = False
    return a
    
    
def is_pandigital(nr, n):
    digits = ''.join(map(str, range(1, n + 1)))
    nr = str(nr)
    for i in digits:
        if str(i) not in nr[0:9]:
            return False
        if str(i) not in nr[-9:]:
            return False

    return True


# In[6]:


largest = 0
for i in Esieve(987654321):
    if is_pandigital(i, len(i)) and i>largest:
        largest=i
        
print(largest)
        


# In[5]:





# In[ ]:




