# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import json
import os
#import readability
import textstat
import matplotlib.pyplot as plt
import numpy as np

countFile = 0
countPolicyText = 0
db={}
formulas = ["FKG", "FRES", "NDC", "GFI", "SMOG"]
northeastStates = ["ME", "NH", "VT", "MA", "CT", "RI", "NY", "PA", "NJ"]
southStates = ["MD", "DE", "WV", "VA", "KY", "NC", "TN", "SC", "GA", "FL", "AL", "MS", "AR", "LA", "OK", "TX"]
midwestStates = ["OH", "MI", "IN", "WI", "IL", "MN", "IA", "MO", "ND", "SD", "NE", "KS"]
westStates = ["MT", "WY", "CO", "NM", "ID", "UT", "AZ", "WA", "OR", "CA"]



FKGScores = {}
FRESScores = {}
NDCScores = {}
GFIScores = {}
SMOGScores = {}

#Scores = {"FKGScores":FKGScores, "FRESScores":FRESScores, "NDCScores":NDCScores, "GFIScores":GFIScores, "SMOGScores":SMOGScores}
#step = 1
for dirPath, dirNames, fileNames in os.walk(r"C:\Users\Lee\csc533-project\data", topdown=False):
    #print(dirPath)
    #print(dirNames)
    #print(dirPath[-2:])
    #print(step)
    #step += 1
    for f in fileNames:
        #print(os.path.join(dirPath, f))
        #print(dirPath[36:])
        #print(dirNames)
        if f == "privacy_policy.json":
            countFile += 1
            with open(os.path.join(dirPath, f), 'r', encoding='utf-8') as json_file:
                data = json.load(json_file)
                for key1, value1 in data.items():
                    for element in value1:
                        #print(dirPath[36:])
                        #print(element["policy_text"])
                        stateName = dirPath[33:35]
                        try:
                            FKG = textstat.flesch_kincaid_grade(element["policy_text"])
                            FRES = textstat.flesch_reading_ease(element["policy_text"])
                            NDC = textstat.dale_chall_readability_score(element["policy_text"])
                            GFI = textstat.gunning_fog(element["policy_text"])
                            SMOG = textstat.smog_index(element["policy_text"])
                            record = {'FKG':FKG, 'FRES':FRES, 'NDC':NDC, 'GFI':GFI, 'SMOG':SMOG}
                            #db[dirPath[36:]] = record
                            print(dirPath[36:])
                            print(FKG, FRES, NDC, GFI, SMOG)
                            countPolicyText += 1
                            
                            FKGScores[dirPath[36:]] = FKG
                            FRESScores[dirPath[36:]] = FRES
                            NDCScores[dirPath[36:]] = NDC
                            GFIScores[dirPath[36:]] = GFI
                            SMOGScores[dirPath[36:]] = SMOG
                            
                            if stateName in northeastStates:
                                region = "NorthEast"
                            elif stateName in southStates:
                                region = "South"
                            elif stateName in midwestStates:
                                region = "MidWest"
                            elif stateName in westStates:
                                region = "West"
                            
                            record["region"] = region
                            db[dirPath[36:]] = record
                            #print(score)
                            #db[dirPath[36:]] = score
                            """
                                score = readability.getmeasures(element["policy_text"], lang="en")
                                
                                #print(dirPath[36:])
                                #print(score['readability grades']['FleschReadingEase'])
                                
                                if score['readability grades']['FleschReadingEase'] < 0:
                                    print(dirPath[36:])
                                    print(score['readability grades']['FleschReadingEase'])
                                
                                db[dirPath[36:]] = score['readability grades']['FleschReadingEase']
                                #for key2, value2 in element.items():
                                #    print(0)
                                """
                        except:
                            if dirPath[36:] not in db:
                                print(dirPath[36:])
                                print("None")
                                #pass
                                #db[dirPath[36:]] = None
                            #pass
                    break
                    print(0)

Scores = {"FKGScores":FKGScores, "FRESScores":FRESScores, "NDCScores":NDCScores, "GFIScores":GFIScores, "SMOGScores":SMOGScores}
count = [0,0,0,0,0]
countNDC = 0
for key, value in db.items():
    if value["FKG"] >= 8:
        count[0] += 1
    if value["FRES"] <= 70:
        count[1] += 1
    if value["NDC"] >= 6.9:
        count[2] += 1
    if value["GFI"] >= 8:
        count[3] += 1
    if value["SMOG"] >= 8:
        count[4] += 1

"""
print("Above 8th grade")
print("FKG: ", count[0]/countPolicyText)
print("FRES: ", count[1]/countPolicyText)
print("NDC: ", count[2]/countPolicyText)
print("GFI: ", count[3]/countPolicyText)
print("SMOG: ", count[4]/countPolicyText)
"""


##################

#category = {}
categories = {}

for key1, value1 in Scores.items():
    category = {}
    category.clear()
    if key1 != "FRESScores":
        #category = {}
        for key2, value2 in value1.items():
            for i in range(0,50,1):
                if value2 < i:
                    category_Name = "[" + str(i) + "," + str(i+1) + ")"
                    if category_Name in category:
                        category[category_Name] += 1
                    else:
                        category[category_Name] = 1
                    break
            #print(key1)
            #print(category)
        if key1 == "FKGScores":
            categories["FKGScores"] = category
        elif key1 == "NDCScores":
            categories["NDCScores"] = category
        elif key1 == "GFIScores":
            categories["GFIScores"] = category
        elif key1 == "SMOGScores":
            categories["SMOGScores"] = category
    else:
        #category = {}
        for key2, value2 in value1.items():
            for i in range(0,100,10):
                if value2 < i:
                    category_Name = "[" + str(i) + "," + str(i+10) + ")"
                    if category_Name in category:
                        category[category_Name] += 1
                    else:
                        category[category_Name] = 1
                    break
            #print(category)
        if key1 == "FRESScores":
            categories["FRESScores"] = category


for key1, value1 in categories.items():
    x = []
    y = []
    for key2, value2 in value1.items():
        x.append(key2)
        y.append(value2)
    fig = plt.figure(figsize=(18,8))
    plt.bar(x, y, label = key1)
    #plt.tick_params(axis='x', labelsize=4)
    #fig = plt.figure(figsize=(12,4))
    plt.legend()
    plt.show()
"""
northeast = []
south = []
midwest = []
west = []

for key1, value1 in db.items():
    if value1["region"] == "northeast":
        
    elif value1["region"] == "south":
        
    elif value1["region"] == "midwest":
        
    elif value1["region"] == "west":
        
    
    
    value1["FKG"]
    value1["FRES"]
    value1["GFI"]
    value1["NDC"]
    value1["SMOG"]
"""
