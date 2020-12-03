#!/usr/bin/env python
# coding: utf-8

# In[3]:


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
from nltk import tokenize
from itertools import islice
from scipy import stats

countFile = 0
countPolicyText = 0
db={}
formulas = ["FKG", "FRES", "NDC", "GFI", "SMOG"]
northeastStates = ["ME", "NH", "VT", "MA", "CT", "RI", "NY", "PA", "NJ"]
southStates = ["MD", "DE", "WV", "VA", "KY", "NC", "TN", "SC", "GA", "FL", "AL", "MS", "AR", "LA", "OK", "TX"]
midwestStates = ["OH", "MI", "IN", "WI", "IL", "MN", "IA", "MO", "ND", "SD", "NE", "KS"]
westStates = ["MT", "WY", "CO", "NM", "ID", "UT", "AZ", "WA", "OR", "CA", "HI", "AK"]



FKGScores = {}
FRESScores = {}
NDCScores = {}
GFIScores = {}
SMOGScores = {}

def numberOfSentences(txt):
    #splittedText = tokenize.sent_tokenize(txt)
    count = 0
    #for line in splittedText:
    for line in txt:
        count += 1
    return count


def findNextTenSentences(txt, nthLine):
    count = 1
    extractText = ""
    for line in txt:
        if count >= nthLine:
            extractText += line
            extractText += "\n"
            #print(line)
        count += 1
        if count == nthLine + 10:
            break
    return extractText
    #for line in islice(txt, nthLine):
    #    print(line)

def extractTextForSMOG(txt):
    splittedText = tokenize.sent_tokenize(txt)
    numOfSentences = numberOfSentences(splittedText)
    if numOfSentences < 30:
        return None
    beginning = findNextTenSentences(splittedText, 10)
    middle = findNextTenSentences(splittedText, int(numOfSentences/2) - 5)
    end = findNextTenSentences(splittedText, numOfSentences-10)
    return beginning + middle + end

def smog_cal(txt):
    if extractTextForSMOG(txt) is None:
        return 0
    else:
        return textstat.smog_index(extractTextForSMOG(txt))

#for dirPath, dirNames, fileNames in os.walk(r"../data", topdown=False):
for dirPath, dirNames, fileNames in os.walk(r"C:\Users\Lee\csc533-project\data", topdown=False):
    for f in fileNames:
        if f == "privacy_policy.json":
            countFile += 1
            with open(os.path.join(dirPath, f), 'r', encoding='utf-8') as json_file:
                data = json.load(json_file)
                for key1, value1 in data.items():
                    for element in value1:
                        stateName = dirPath[33:35]
                        try:
                            if element["is_covid_specific"] is True:
                                FKG = textstat.flesch_kincaid_grade(element["policy_text"])
                                FRES = textstat.flesch_reading_ease(element["policy_text"])
                                NDC = textstat.dale_chall_readability_score(element["policy_text"])
                                GFI = textstat.gunning_fog(element["policy_text"])
                                SMOG = smog_cal(element["policy_text"])
                                record = {'FKG':FKG, 'FRES':FRES, 'NDC':NDC, 'GFI':GFI, 'SMOG':SMOG}
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
                        except:
                            if dirPath[36:] not in db:
                                print(dirPath[36:])
                                print("None")
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

##################

categories = {}

for key1, value1 in Scores.items():
    category = {}
    category.clear()
    if key1 != "FRESScores":
        #category = {}
        for key2, value2 in value1.items():
            for i in range(0,50,1):
                if value2 < i:
                    if i < 10:
                        category_Name = "[" + "0" + str(i-1) + "," + "0" + str(i) + ")"
                    elif i == 10:
                        category_Name = "[" + "0" + str(i-1) + "," + str(i) + ")"
                    else:
                        category_Name = "[" + str(i-1) + "," + str(i) + ")"
                    if category_Name in category:
                        category[category_Name] += 1
                    else:
                        category[category_Name] = 1
                    break
        if key1 == "FKGScores":
            categories["FKGScores"] = category
        elif key1 == "NDCScores":
            categories["NDCScores"] = category
        elif key1 == "GFIScores":
            categories["GFIScores"] = category
        elif key1 == "SMOGScores":
            categories["SMOGScores"] = category
    else:
        for key2, value2 in value1.items():
            for i in range(0,100,10):
                if value2 < i:
                    if i < 10:
                        category_Name = "[" + "0" + str(i-1) + "," + "0" + str(i) + ")"
                    elif i == 10:
                        category_Name = "[" + "0" + str(i-1) + "," + str(i) + ")"
                    else:
                        category_Name = "[" + str(i-1) + "," + str(i) + ")"
                    if category_Name in category:
                        category[category_Name] += 1
                    else:
                        category[category_Name] = 1
                    break
        if key1 == "FRESScores":
            categories["FRESScores"] = category


scoresTypes = ["FKG", "FRES", "GFI", "NDC", "SMOG"]

FKG = []
FRES = []
GFI = []
NDC = []
SMOG = []

regionScores = [FKG, FRES, GFI, NDC, SMOG]

i = 0
for scoresType in scoresTypes:
    northeast = []
    south = []
    midwest = []
    west = []
    for key, value in db.items():
        if value["region"] == "NorthEast":
            northeast.append(value[scoresType])
        elif value["region"] == "South":
            south.append(value[scoresType])
        elif value["region"] == "MidWest":
            midwest.append(value[scoresType])
        elif value["region"] == "West":
            west.append(value[scoresType])
    regionScores[i].append({"northeast":northeast, "south":south, "midwest":midwest, "west":west})
    i += 1


plt.rcParams.update({'font.size': 30})
scoreName = 0
for i in regionScores:
    y = [stats.trim_mean(i[0]["northeast"], 0.25), stats.trim_mean(i[0]["south"], 0.25), 
             stats.trim_mean(i[0]["midwest"], 0.25), stats.trim_mean(i[0]["west"], 0.25)]
    x = [f"{round(stats.trim_mean(i[0]['northeast'], 0.25),2)}\nNortheast", f"{round(stats.trim_mean(i[0]['south'], 0.25),2)}\nSouth", f"{round(stats.trim_mean(i[0]['midwest'], 0.25),2)}\nMidwest", f"{round(stats.trim_mean(i[0]['west'], 0.25),2)}\nWest"]
    fig = plt.figure(figsize=(18,8))
    plt.bar(x, y)
    plt.ylabel("Readability Score - Midquartile")
    plt.xlabel("Regions")
    plt.title(f"{scoresTypes[scoreName]} Readability Scores of Privacy Policies")
    plt.savefig(f'C:\\Users\\Lee\\csc533-project\\figures\\readability-score-{scoresTypes[scoreName]}-regions.png')
    scoreName += 1


for key1, value1 in categories.items():
    if key1 == "SMOGScores":
        x = list(value1.keys())
        y = []
        x.sort()
        x.remove("[00,01)")
        for key2 in x:
            if key2 != "[00,01)":
                y.append(value1[key2])
        pass
    else:
        x = list(value1.keys())
        y = []
        x.sort()    
        for key2 in x:
            y.append(value1[key2])
    
    if key1 == "GFIScores" or key1 == "FKGScores":
        #plt.rcParams.update({'font.size': 16})
        fig = plt.figure(figsize=(18,9.5))
        plt.bar(x, y)
        plt.xticks(fontsize = 22, rotation = 20)
        plt.yticks(fontsize = 30)
    else:
        fig = plt.figure(figsize=(18,8))
        plt.bar(x, y)
        plt.xticks(fontsize = 30)
        plt.yticks(fontsize = 30)
    plt.xlabel("Readability Score", fontsize=30)
    plt.ylabel("Number of Occurances", fontsize=30)
    plt.title(f"{key1[:-6]} Readability Scores of Privacy Policies", fontsize=30)
    
    #plt.savefig(f'../figures/readability-score-{key1}.png')
    plt.savefig(f'C:\\Users\\Lee\\csc533-project\\figures\\readability-score-{key1}.png')
    plt.show()


# In[29]:

plt.rcParams.update({'font.size': 30})
key = 'FRESScores'
scores = categories[key]

x = list(categories[key].keys())
y = []
x.sort(reverse=True)    
for key2 in x:
    y.append(scores[key2])

fig = plt.figure(figsize=(18,8))
plt.bar(x, y)
plt.xlabel("Readability Score")
plt.ylabel("Number of Occurances")
plt.title(f"{key[:-6]} Readability Scores of Privacy Policies")

#plt.savefig(f'../figures/readability-score-{key}.png')
plt.savefig(f'C:\\Users\\Lee\\csc533-project\\figures\\readability-score-{key}.png')
plt.show()


# In[ ]:
#number of schools with privacy_policy.get("policy_text") / # schools with has_self_reporting_site= True

northeastSchoolsWithPrivacyPolicy = []
southSchoolsWithPrivacyPolicy = []
midwestSchoolsWithPrivacyPolicy = []
westSchoolsWithPrivacyPolicy = []

for university, value in db.items():
    if value["region"] == "NorthEast":
        northeastSchoolsWithPrivacyPolicy.append(university)
    elif value["region"] == "South":
        southSchoolsWithPrivacyPolicy.append(university)
    elif value["region"] == "MidWest":
        midwestSchoolsWithPrivacyPolicy.append(university)
    elif value["region"] == "West":
        westSchoolsWithPrivacyPolicy.append(university)

northeastSchools = []
southSchools = []
midwestSchools = []
westSchools = []

northeastSchoolsWithSelfReporting = []
southSchoolsWithSelfReporting = []
midwestSchoolsWithSelfReporting = []
westSchoolsWithSelfReporting = []

for dirPath, dirNames, fileNames in os.walk(r"C:\Users\Lee\csc533-project\data", topdown=False):
    for f in fileNames:
        if f == "privacy_policy.json":
            with open(os.path.join(dirPath, f), 'r', encoding='utf-8') as json_file:
                stateName = dirPath[33:35]
                schoolName = dirPath[36:]
                
                if stateName in northeastStates:
                    northeastSchools.append(schoolName)
                elif stateName in southStates:
                    southSchools.append(schoolName)
                elif stateName in midwestStates:
                    midwestSchools.append(schoolName)
                elif stateName in westStates:
                    westSchools.append(schoolName)
        if f == "guidelines.json":
            with open(os.path.join(dirPath, f), 'r', encoding='utf-8') as json_file:
                data = json.load(json_file)
                #print(data)
                if data["self_reporting"] is not None:
                    #print(data["self_reporting"])
                    stateName = dirPath[33:35]
                    schoolName = dirPath[36:]
                    if stateName in northeastStates:
                        northeastSchoolsWithSelfReporting.append(schoolName)
                    elif stateName in southStates:
                        southSchoolsWithSelfReporting.append(schoolName)
                    elif stateName in midwestStates:
                        midwestSchoolsWithSelfReporting.append(schoolName)
                    elif stateName in westStates:
                        westSchoolsWithSelfReporting.append(schoolName)


y = [len(northeastSchoolsWithPrivacyPolicy)*100/len(northeastSchoolsWithSelfReporting), 
     len(southSchoolsWithPrivacyPolicy)*100/len(southSchoolsWithSelfReporting), 
     len(midwestSchoolsWithPrivacyPolicy)*100/len(midwestSchoolsWithSelfReporting), 
     len(westSchoolsWithPrivacyPolicy)*100/len(westSchoolsWithSelfReporting)]
x = [f"{round(y[0], 2)}%\nNorthEast", f"{round(y[1], 2)}%\nSouth", f"{round(y[2], 2)}%\nMidwest", f"{round(y[3], 2)}%\nWest"]
plt.rcParams.update({'font.size': 30})
fig = plt.figure(figsize=(18,8))
plt.bar(x, y)
plt.xlabel("Regions")
plt.ylabel("Percentage of schools with privacy policy")
plt.title("Percentage of schools with privacy policy within each region")

#plt.savefig(f'../figures/readability-score-{key}.png')
plt.savefig('C:\\Users\\Lee\\csc533-project\\figures\\percentage-of-schools-with-privacy-policy-in-each-region.png')
plt.show()

y = [len(northeastSchoolsWithSelfReporting)*100/len(northeastSchools), 
     len(southSchoolsWithSelfReporting)*100/len(southSchools), 
     len(midwestSchoolsWithSelfReporting)*100/len(midwestSchools), 
     len(westSchoolsWithSelfReporting)*100/len(westSchools)]
x = [f"{round(y[0], 2)}%\nNorthEast", f"{round(y[1], 2)}%\nSouth", f"{round(y[2], 2)}%\nMidwest", f"{round(y[3], 2)}%\nWest"]
plt.rcParams.update({'font.size': 30})
fig = plt.figure(figsize=(18,8))
plt.bar(x, y)
plt.xlabel("Regions")
plt.ylabel("Percentage of schools with self reporting")
plt.title("Percentage of schools with self reporting within each region")

plt.savefig('C:\\Users\\Lee\\csc533-project\\figures\\percentage-of-schools-with-self-reporting-in-each-region.png')
plt.show()
