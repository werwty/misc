#!/usr/bin/env python
# coding: utf-8

# In[5]:



import os


employers = ('Private', 'Self-emp-not-inc', 'Self-emp-inc', 'Federal-gov',
             'Local-gov', 'State-gov', 'Without-pay', 'Never-worked')
maritals = ('Married-civ-spouse', 'Divorced', 'Never-married', 'Separated',
            'Widowed', 'Married-spouse-absent', 'Married-AF-spouse')
occupations = ('Tech-support', 'Craft-repair', 'Other-service', 'Sales',
               'Exec-managerial', 'Prof-specialty', 'Handlers-cleaners', 'Machine-op-inspct',
               'Adm-clerical', 'Farming-fishing', 'Transport-moving', 'Priv-house-serv',
               'Protective-serv', 'Armed-Forces')
races = ('White', 'Asian-Pac-Islander','Amer-Indian-Eskimo', 'Other', 'Black')
sexes = ('Female', 'Male')
countries = ('United-States', 'Cambodia', 'England', 'Puerto-Rico',
            'Canada', 'Germany', 'Outlying-US(Guam-USVI-etc)', 'India', 'Japan', 'Greece',
            'South', 'China', 'Cuba', 'Iran', 'Honduras', 'Philippines', 'Italy', 'Poland',
            'Jamaica', 'Vietnam', 'Mexico', 'Portugal', 'Ireland', 'France',
            'Dominican-Republic', 'Laos', 'Ecuador', 'Taiwan', 'Haiti', 'Columbia',
            'Hungary', 'Guatemala', 'Nicaragua', 'Scotland', 'Thailand', 'Yugoslavia',
            'El-Salvador', 'Trinadad&Tobago', 'Peru', 'Hong', 'Holand-Netherlands')

featureNames = (('age','sex') + employers + ('education',) + maritals + occupations +
               races + ('capital_gain','capital_loss','hr_per_week') + countries)


## vectorize data: assigns 1 if the value matches otherwise 0 (flattens categorical values as individual features)
## something like one-hot-encoding
def vectorize(value, values):
    return [int(v==value) for v in values]


## vectorize categorical values
## output format: features, label
def processLine(line):
    values = line.strip().split(', ')
    (age, employer, _, _, education, marital, occupation, _, race, sex,
      capital_gain, capital_loss, hr_per_week, country, income) = values

    # put sex second so I know what index it is
    point = ([int(age), 0 if sex=='Female' else 1] + vectorize(race, races) + vectorize(employer, employers) 
            + [int(education)] + vectorize(marital, maritals) + vectorize(occupation, occupations) +
            [int(capital_gain), int(capital_loss), int(hr_per_week)] + vectorize(country, countries))
    label = 1 if income[0] == '>' else -1

    return tuple(point), label


## Load data as array of (feature, label) 
def load(name):
    with open(name, 'r') as infile:
        Data = [processLine(line) for line in infile]
        Points, Labels = zip(*Data)
        return Points, Labels





# In[15]:


datas, labels = load('adult_data.txt')


# In[63]:


print("3a.")
protected_data = []
protected_labels = []

nonprotected_data = []
nonprotected_labels = []

for i, data in enumerate(datas):
    # not female
    if data[1]:
        nonprotected_data.append(data)
        nonprotected_labels.append(labels[i])
    # female
    else:
        protected_data.append(data)
        protected_labels.append(labels[i])

        
#PR(output | s) = pr(output)*pr(s|output)/pr(s)
total_1 = len([label for label in labels if label==1])
number_data = len(labels)

# Pr(output=1)
p_outcome_1 = total_1/number_data

# pr(s)
p_s = len(protected_labels)/number_data

# pr(s|output=1)
p_s_given_1 = len([label for label in protected_labels if label==1])/total_1

# pr(output=1 | s)
p_1_given_s = p_outcome_1*p_s_given_1/p_s

p_sc = len(nonprotected_labels)/number_data
p_sc_given_1 = len([label for label in nonprotected_labels if label==1])/total_1
p_1_given_sc = p_outcome_1*p_sc_given_1/p_sc

print(f"Pr(>50k|Female) = {p_1_given_s}")
print(f"Pr(>50k|Male) = {p_1_given_sc}")
print(f"|Pr(>50k|Female)- Pr(>50k|Male)| = {abs(p_1_given_s-p_1_given_sc)}")
total_0 = len([label for label in labels if label==-1])
p_outcome_0 = total_0/number_data
p_s_given_0 = len([label for label in protected_labels if label==-1])/total_0
p_0_given_s = p_outcome_0*p_s_given_0/p_s


p_sc_given_0 = len([label for label in nonprotected_labels if label==-1])/total_0
p_0_given_sc = p_outcome_0*p_sc_given_0/p_sc

print(f"Pr(<50k|Female) = {p_0_given_s}")
print(f"Pr(<50k|Male) = {p_0_given_sc}")
print(f"|Pr(<50k|Female)- Pr(<50k|Male)| = {abs(p_0_given_s-p_0_given_sc)}")

## TODOs ##

## determine statictical parity in terms of protected group for 1) gender [female being the protected group] 
## and 2) race [asian people being the protected group]
## compute (print out) the probabilistic difference between the protected group and non-protected group
## if the difference is close to zero (let us say 0.05 difference) then you have statistical partity, 
## if not you don't have statistical parity 

# (('age','sex') + employers + ('education',) + maritals + occupations + races + ('capital_gain','capital_loss','hr_per_week') + countries)


# In[66]:


print("3b")
nonprotected_data = []
nonprotected_labels = []

for i, data in enumerate(datas):
    # asian
    if data[3]:
        protected_data.append(data)
        protected_labels.append(labels[i])
    # not asian
    else:
        nonprotected_data.append(data)
        nonprotected_labels.append(labels[i])

total_1 = len([label for label in labels if label==1])
number_data = len(labels)


p_outcome_1 = total_1/number_data
p_s = len(protected_labels)/number_data
p_s_given_1 = len([label for label in protected_labels if label==1])/total_1
p_1_given_s = p_outcome_1*p_s_given_1/p_s

p_sc = len(nonprotected_labels)/number_data
p_sc_given_1 = len([label for label in nonprotected_labels if label==1])/total_1
p_1_given_sc = p_outcome_1*p_sc_given_1/p_sc

print(f"Pr(>50k|Asian) = {p_1_given_s}")
print(f"Pr(>50k|not Asian) = {p_1_given_sc}")
print(f"|Pr(>50k|Asian)- Pr(>50k|Not asian)| = {abs(p_1_given_s-p_1_given_sc)}")
total_0 = len([label for label in labels if label==-1])
p_outcome_0 = total_0/number_data
p_s_given_0 = len([label for label in protected_labels if label==-1])/total_0
p_0_given_s = p_outcome_0*p_s_given_0/p_s


p_sc_given_0 = len([label for label in nonprotected_labels if label==-1])/total_0
p_0_given_sc = p_outcome_0*p_sc_given_0/p_sc

print(f"Pr(<50k|Asian) = {p_0_given_s}")
print(f"Pr(<50k|Not Asian) = {p_0_given_sc}")
print(f"|Pr(<50k|Asian)- Pr(<50k|Not Asian)| = {abs(p_0_given_s-p_0_given_sc)}")


# In[62]:





# In[ ]:




