#!/usr/bin/env python
# coding: utf-8

# In[38]:


import math


# In[58]:


def calculate_mg_week(
    age, 
    height, 
    weight, 
    vkorc1, 
    cyp2c9, 
    race, 
    enzyme_inducer, 
    amiodarone
):
    age_dec = int(str(age)[0])
    
    vkorc1_ag = 0
    vkorc1_aa =0 
    vkorc1_unknown = 0
    if vkorc1 == "A/A":
        vkorc1_aa = 1
    elif vkorc1 == "A/G":
        vkorc1_ag = 1
    elif vkorc1 == "U":
        vkorc1_unknown=1
    cyp2c9_12 =0 
    cyp2c9_13 =0
    cyp2c9_22 =0
    cyp2c9_23 =0
    cyp2c9_33=0
    cyp2c9_unknown =0
    
    if cyp2c9 == "*1/*2":
        cyp2c9_12 = 1
    elif cyp2c9 == "*1/*3":
        cyp2c9_13 = 1
    elif cyp2c9 == "*2/*2":
        cyp2c9_22 = 1
    elif cyp2c9 == "*2/*3":
        cyp2c9_23 = 1
    elif cyp2c9 == "*3/*3":
        cyp2c9_33 = 1
    elif cyp2c9 == "U":
        cyp2c9_unknown=1
        
    asian =0
    black =0
    missing_race =0
    if race =="A":
        asian =1
    elif race == "B":
        black =1
    elif race == "U":
        missing_race = 1
    
    enzyme_inducer_status =0 
    if enzyme_inducer == "Y":
        enzyme_inducer_status =1 
    
    amiodarone_status =0 
    if amiodarone == "Y":
        amiodarone_status = 1
        
    mg_wk = 5.6044 -     0.2614*age_dec +     0.0087*height +     0.0128*weight -     0.8677*vkorc1_ag -     1.6974*vkorc1_aa -     0.4854*vkorc1_unknown -    0.5211*cyp2c9_12 -    0.9357 * cyp2c9_13 -     1.0616 * cyp2c9_22 -    1.9206 * cyp2c9_23 -    2.3312*cyp2c9_33 -    0.2188 * cyp2c9_unknown -     0.1092*asian -     0.2760*black -     0.1032* missing_race +    1.1816*enzyme_inducer_status -    0.5503 * amiodarone_status
    
    mg_wk =  math.pow(mg_wk, 2)

    return mg_wk


def find_genotypes(dose, age, height, weight, race, enzyme_inducer, amiodarone):
    possible_vkorc1 = ["A/A", "A/G", "G/G", "U"]
    possible_cyp2c9 = ["*1/*1", "*1/*2", "*1/*3", "*2/*2", "*2/*3", "*3/*3", "U"]
    
    all_genotypes = {}
    
    for vkorc1 in possible_vkorc1:
        for cyp2c9 in possible_cyp2c9:
            dosage = calculate_mg_week(age = age, 
                  height = height, 
                  weight = weight, 
                  vkorc1 = vkorc1, 
                  cyp2c9 = cyp2c9, 
                  race = race, 
                  enzyme_inducer = enzyme_inducer, 
                  amiodarone = amiodarone)
            all_genotypes[(vkorc1, cyp2c9)] = dosage
    
    sorted_genotypes = {k: v for k, v in sorted(all_genotypes.items(), key=lambda item: abs(item[1]-dose))}
    return sorted_genotypes
            


# In[61]:


bob_genotype = find_genotypes(dose = 21, 
               age = 56, 
               height = 177.8, 
               weight = 72,                   
               race = "C", 
               enzyme_inducer = "Y", 
               amiodarone = "Y")
print("Bob's top 3 probably genotpye combinations:")
print(f"Genotype: {list(bob_genotype.keys())[0]}, Warfarin dose: {bob_genotype[list(bob_genotype.keys())[0]]}")
print(f"Genotype: {list(bob_genotype.keys())[1]}, Warfarin dose: {bob_genotype[list(bob_genotype.keys())[1]]}")
print(f"Genotype: {list(bob_genotype.keys())[2]}, Warfarin dose: {bob_genotype[list(bob_genotype.keys())[2]]}")


# In[ ]:





# In[ ]:




