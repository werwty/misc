import re, sys
import math, random
import numpy as np
import operator

#### BEGIN----- functions to read movie files and create db ----- ####

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

def score(w, p, aux, r):
    '''
    Inputs: weights of movies, max rating per moive, auxiliary information, and a record, 
    Returns the corresponding score
    '''
    #### ----- your code here ----- ####

    pass



def compute_weights(db):
    '''
    Input: database of users
    Returns weights of all movies
    '''
    #### ----- your code here ----- ####

    ## you can use 10 base log

    pass



#### BEGIN----- additional functions ----- ####



#### END----- additional functions ----- ####

if __name__ == "__main__":
    db = {}
    files = ["03124", "06315", "07242", "16944", "17113",
            "10935", "11977", "03276", "14199", "08191",
            "06004", "01292", "15267", "03768", "02137"]

    for file in files:
        read_files(db, file)

    aux = { '14199': 4.5, '17113': 4.2, '06315': 4.0, '01292': 3.3,
            '11977': 4.2, '15267': 4.2, '08191': 3.8, '16944': 4.2,
            '07242': 3.9, '06004': 3.9, '03768': 3.5, '03124': 3.5}

    #### ----- your code here ----- ####



    
