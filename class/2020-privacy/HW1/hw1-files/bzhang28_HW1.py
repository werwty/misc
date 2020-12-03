#!/usr/bin/env python
# coding: utf-8

# In[1]:


import re, sys
import math, random
import numpy as np
import operator

from pprint import pprint
from collections import namedtuple


# In[2]:


def add_ratings(db, chunks, num):
    if not chunks[0] in db:
        db[chunks[0]] = {}
    db[chunks[0]][num] = int(chunks[2])

def read_files(db, num):
    movie_file = "movies/"+num
    ratings = []
    fo = open(movie_file, "r")
    r = 0
    for line in fo:
        chunks = re.split(",", line)
        chunks[len(chunks)-1] = chunks[len(chunks)-1].strip()
        add_ratings(db, chunks, num)

#### END----- functions to read movie files and create db ----- ####


# In[14]:


def score(movies):
    '''
    Inputs: weights of movies, max rating per moive, auxiliary information, and a record, 
    Returns the corresponding score
    '''
    #### ----- your code here ----- ####

    movie_score = 0 
    
    supp = 12
        
    for movie in movies:
        w = movie.weight
        p = movie.p
        aux = movie.aux
        r = movie.rating
        id = movie.id
        
        if r is None:
            continue

        T = 1- (abs(aux - r)/p)
        #print(f"Calculating score for {id}, {movie_score}, {w*T/supp}")

        movie_score = movie_score + w*T/supp
   
    return movie_score



def compute_weights(db):
    '''
    Input: database of users
    Returns weights of all movies
    '''
    #### ----- your code here ----- ####

    ## you can use 10 base log
    
    # dict with movie_id as key and frequency as value
    movie_freq = {}
    for user, movies in db.items():
        for movie,ratings in movies.items():
            if not movie in movie_freq:
                movie_freq[movie]=1
            else:
                movie_freq[movie]=movie_freq[movie]+1
    
    weights = {}
    for movie, freq in movie_freq.items():
        weights[movie]=1/math.log10(freq)
        
    return weights
        

def compute_p(db, aux):
    '''
    Input: database of users
    Returns weights of all movies
    '''
    #### ----- your code here ----- ####

    ## you can use 10 base log
    
    # dict with movie_id as key and frequency as value
    movie_rating_range = {}
    for user, movies in db.items():
        for movie, rating in movies.items():
            if movie not in movie_rating_range:
                movie_rating_range[movie] = set()            
            movie_rating_range[movie].add(rating)
            
    movie_rating_p = {}
    for movie, rating_range in movie_rating_range.items():
        aux_rating = aux.get(movie, None)
        if aux_rating is not None:
            rating_range.add(aux_rating)
        movie_rating_p[movie] = (max(rating_range)- min(rating_range))
            
    return movie_rating_p
        


# In[15]:


db = {}
files = ["03124", "06315", "07242", "16944", "17113",
        "10935", "11977", "03276", "14199", "08191",
        "06004", "01292", "15267", "03768", "02137"]

for file in files:
    read_files(db, file)

MovieInfo = namedtuple("MovieInfo", 'id, aux, rating, weight, p')

auxes = { '14199': 4.5, '17113': 4.2, '06315': 4.0, '01292': 3.3,
        '11977': 4.2, '15267': 4.2, '08191': 3.8, '16944': 4.2,
        '07242': 3.9, '06004': 3.9, '03768': 3.5, '03124': 3.5}


# In[16]:


# Question a
weights = compute_weights(db)
print("Question 1a, Weights")
print("Movie ID, weight")
for movie, freq in weights.items():
    print(f"{movie}, {freq}")
ps = compute_p(db, auxes)


# In[17]:


# Question b
similarity_scores = []
for user, movies in db.items():    
    movies_to_score = []
    for id, aux in auxes.items():
        p = ps.get(id)
        weight = weights.get(id)
        rating = movies.get(id)
        movie = MovieInfo(
            id=id, 
            aux=aux, 
            weight=weight, 
            rating=rating, 
            p=p
        )
        movies_to_score.append(movie)
    #print(user)
    similarity_scores.append((user, score(movies_to_score)))
    
    


# In[27]:


similarity_scores = sorted(similarity_scores, key = lambda x: x[1], reverse=True)
print("\nQuestion 1b, top 5 similartity scores to aux")
print("User ID, score")
for simscore in similarity_scores[:5]:
    print(f"{simscore[0]}, {simscore[1]}")


# In[26]:


print("\nQuestion 1c, Ratings of user with highest similarity score")
print("Movie ID, Top User Rating, AUX")
for movie, aux in auxes.items():
    print(f"{movie}, {db.get(similarity_scores[0][0]).get(movie)}, {aux}")


# In[36]:


# Question 1d
def calculate_M(weights, auxes):
    supp=12
    M=0
    for movie_id, aux in auxes.items():
        M = M + weights[movie_id]/12
    return M

M = calculate_M(weights, auxes)

print("\nQuestion 1d")
print("a.")
y = .1
print(f"if y is {y}, M is {M}, the difference between highest and second "
      f"highest similarity score is {similarity_scores[0][1]-similarity_scores[1][1]}. "
     f"y*M is {y*M}. {similarity_scores[0][1]-similarity_scores[1][1]} > {y*M} is"
     f" {similarity_scores[0][1]-similarity_scores[1][1] > y*M}")


print("b.")
y = .05

print(f"if y is {y}, M is {M}, the difference between highest and second "
      f"highest similarity score is {similarity_scores[0][1]-similarity_scores[1][1]}. "
     f"y*M is {y*M}. {similarity_scores[0][1]-similarity_scores[1][1]} > {y*M} is"
     f" {similarity_scores[0][1]-similarity_scores[1][1] > y*M}")


# In[ ]:




