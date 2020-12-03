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

countFile = 0
db={}
for dirPath, dirNames, fileNames in os.walk(r"C:\Users\Lee\csc533-project\data", topdown=False):
    #print(dirPath)
    for f in fileNames:
        #print(os.path.join(dirPath, f))
        #print(dirPath[36:])
        if f == "privacy_policy.json":
            countFile += 1
            with open(os.path.join(dirPath, f), 'r', encoding='utf-8') as json_file:
                data = json.load(json_file)
                for key1, value1 in data.items():
                    for element in value1:
                        #print(dirPath[36:])
                        #print(element["policy_text"])
                        try:
                            FKG = textstat.flesch_kincaid_grade(element["policy_text"])
                            FRES = textstat.flesch_reading_ease(element["policy_text"])
                            NDC = textstat.dale_chall_readability_score(element["policy_text"])
                            GFI = textstat.gunning_fog(element["policy_text"])
                            SMOG = textstat.smog_index(element["policy_text"])
                            record = {'FKG':FKG, 'FRES':FRES, 'NDC':NDC, 'GFI':GFI, 'SMOG':SMOG}
                            db[dirPath[36:]] = record
                            print(dirPath[36:])
                            print(FKG, FRES, NDC, GFI, SMOG)
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


count = [0,0,0,0,0]
countNDC = 0
for key, value in db.items():
    if value["FKG"] > 70:
        count[0] += 1
    if value["FRES"] < 70:
        count[1] += 1
    if value["NDC"] > 6.9:
        count[2] += 1
    if value["GFI"] >8:
        count[3] += 1
    if value["SMOG"] >8:
        count[4] += 1

print("Above 8th grade")
print("FKG: ", count[0]/countFile)
print("FRES: ", count[1]/countFile)
print("NDC: ", count[2]/countFile)
print("GFI: ", count[3]/countFile)
print("SMOG: ", count[4]/countFile)