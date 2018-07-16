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

#------------------END INPUT/OUTPUT FORMATS-------------------------





#+++++++++++++++++++Script commences below+++++++++++++++++++++++

import csv
import sys
from collections import defaultdict

try:
  infilename = sys.argv[1]
  outfilename = sys.argv[2]

except:
  print ("Usage:",sys.argv[0], "infile outfile")
  sys.exit(1)


#---Dictionaries for the quantities of interest---
prescriber_count        = defaultdict(int)      #number of unique prescribers of a given drug
total_cost              = defaultdict(float)    #total cost of a drug  
avoid_multiple_counting = defaultdict(int)      #Required to ascertain the uniqueness of a presciber



#---------PROCESSING INPUT--------------------------
input_file = open(infilename, 'r') # open file for reading
CSVFILE_INPUT = csv.reader(input_file, delimiter=',')
next(CSVFILE_INPUT) # read first line of ifile (to be ignored)

# begin processind data from second line
for row in CSVFILE_INPUT:
    name=row[1]+'-'+row[2]+'-'+row[3]    #name-drug concatenated variable; dash character guarantees uniqueness
    drug=row[3]                          #extract name of drug that was prescribed
    cost=row[4]                          #extract cost of drug when it was prescribed

    avoid_multiple_counting[name] +=1    #Update home many times a presciber has prescribed the same drug

    if avoid_multiple_counting[name]==1: #Check if this is the first time the prescriber prescibed this drug
       prescriber_count[drug] +=1        #If this is the first time, update the number of UNIQUE prescribers

    total_cost[drug] += float(cost)      #calculate total prescription cost for this drug

input_file.close()
#------------INPUT PROCESSING DONE---------------------




# ---------WRITING OUTPUT--------------------------
output_file = open(outfilename, 'w') # open file for writing
CSVFILE_OUTPUT = csv.writer(output_file, delimiter=',')

header=("drug_name","num_prescriber","total_cost")
CSVFILE_OUTPUT.writerow(header)
for drug in prescriber_count.keys():
    row_output=(drug,prescriber_count[drug],'%.2f' %total_cost[drug])
    CSVFILE_OUTPUT.writerow(row_output)
output_file.close()
#------------INPUT WRITING DONE---------------------

#+++++++++++++++++++End of script+++++++++++++++++++++++++++++++
