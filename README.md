# Raymond Atta-Fynn

# Department of Physics

# The University of Texas at Arlington

# Email: r.attafynn@gmail.com attafynn@uta.edu

# July 14. 2018

# Insight Data Engineering Coding Challenge





#----------BEGIN INPUT/OUTPUT FORMATS---------------------------------



# This script takes an intput of the form:



#id,prescriber_last_name,prescriber_first_name,drug_name,drug_cost

#1000000001,Smith,James,AMBIEN,100

#1000000002,Garcia,Maria,AMBIEN,200

#1000000003,Johnson,James,CHLORPROMAZINE,1000

#1000000004,Rodriguez,Maria,CHLORPROMAZINE,2000

#1000000005,Smith,David,BENZTROPINE MESYLATE,1500



#The output has the form:



#drug_name,num_prescriber,total_cost

#CHLORPROMAZINE,2,3000

#BENZTROPINE MESYLATE,1,1500

#AMBIEN,2,300



# where:

#drug_name: ------> the exact drug name as shown in the input dataset



#num_prescriber:------> the number of UNIQUE PRESCRIBERS who prescribed the drug. 

#(For the purposes of this challenge, a prescriber is considered the same 

# person if two lines share the same prescriber first and last names)



#total_cost:----> total cost of the drug across all prescribers



