#!/usr/bin/env python
# coding: utf-8

# In[493]:


from collections import defaultdict 

class Graph:
  def __init__(self):
    self.V = set()
    self.E = defaultdict(list)
    self.w = {}

  def add_vertex(self, v):
    self.V.add(v)

  def add_edge(self, from_v, to_v, weight):
    self.E[from_v].append(to_v)
    self.E[to_v].append(from_v)
    self.w[(from_v, to_v)] = weight
    self.w[(to_v, from_v)] = weight


# In[494]:


g = Graph()

#number of edges
n = int(input().split()[1])

for i in range(0, n):
    edge = input().split()
    g.add_vertex(edge[0])
    g.add_vertex(edge[1])
    
    g.add_edge(edge[0], edge[1], int(edge[2]))


(source, dest)= input().split()


# In[532]:


import copy

def dijsktra(graph, source, dest):
    v={}
    
    for vertex in graph.V:
        if vertex==source:            
            v[vertex]={'d': 0,
                      'p': None, 
                      'edges': 0,
                      'path':set()}
        else:
            v[vertex]={'d': float('inf'),
                      'p': None, 
                      'edges': 0,
                      'path':set()}
    
    S = {}
    Q = copy.deepcopy(v)
    #print(min(v.items(), key=lambda v: v[1]['d']))
    while len(Q.keys())>0:
        u, random = min(Q.items(), key=lambda x: x[1]['d']) 
        
        uval = v[u]
        S[u]=uval
       
        for adjv in graph.E[u]:
    
        #print('adjacent vertex {} to vertex {}'.format(adjv, u))
            #print(uval)

            #print(v[adjv])

            #print(v[adjv]['d'])
            #print(uval['d'])
            #print( graph.w[(adjv, u)])
            

            #lexographical comparison, if weight is equal, and number of edges are equal
            if v[adjv]['d'] == uval['d'] + graph.w[(adjv, u)] and v[adjv]['edges']== uval['edges']+1 and ' '.join(str(i) for i in list(reversed(list(v[adjv]['path']))))> ' '.join(str(i) for i in list(reversed(list(uval['path'])))):
                #print(' '.join(str(i) for i in list(reversed(list(v[adjv]['path'])))))
                #print(' '.join(str(i) for i in list(reversed(list(uval['path'])))))
                #print(adjv)
                #print(v[adjv])
                #print(uval)
                v[adjv]['d'] = uval['d'] + graph.w[(adjv, u)]
                v[adjv]['p'] = u
                v[adjv]['edges'] += uval['edges'] + 1
                v[adjv]['path']=  uval['path'] or set()
                v[adjv]['path'].add(u)
                Q[adjv]['d'] = uval['d'] + graph.w[(adjv, u)]               

            # if number of edges is smaller...
            elif v[adjv]['d'] == uval['d'] + graph.w[(adjv, u)] and v[adjv]['edges']> uval['edges']+1:
                #print(v[adjv]['edges'])
                #print(' '.join(str(i) for i in list(reversed(uval['path']))))
                v[adjv]['d'] = uval['d'] + graph.w[(adjv, u)]
                v[adjv]['p'] = u
                v[adjv]['edges'] += uval['edges'] + 1
                v[adjv]['path']=  uval['path'] or set()
                v[adjv]['path'].add(u)
                Q[adjv]['d'] = uval['d'] + graph.w[(adjv, u)]               

                
            if v[adjv]['d'] > uval['d'] + graph.w[(adjv, u)]:


                v[adjv]['d'] = uval['d'] + graph.w[(adjv, u)]                
                v[adjv]['p'] = u                
                v[adjv]['edges'] += uval['edges'] + 1                
                v[adjv]['path'] = uval['path'] or set()
                v[adjv]['path'].add(u)
                
                Q[adjv]['d'] = uval['d'] + graph.w[(adjv, u)]               

                


        del Q[u]


    return v


# In[533]:


graph2 = dijsktra(g, source, dest)

def get_path(graph, dest):
    path = [dest]
    while graph[dest]['p'] is not None:
        path.append(graph[dest]['p'])
        dest = graph[dest]['p']
    return list(reversed(path))


# In[535]:


print(graph2[dest]['d'])
path = get_path(graph2, dest)
print(' '.join(str(i) for i in path))
#print(graph2['10'])


# In[ ]:





# In[ ]:




