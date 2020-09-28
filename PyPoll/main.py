#import modules
import csv
import os


#import the resource csv
election_csv = os.path.join("Resources","election_data.csv")

#Variables
candidates = []
votes = []
unique_cand = []


with open(election_csv,"r") as csvdata:
    csvreader = csv.reader(csvdata,delimiter=",")
    #skip header
    next(csvreader)
    
    for row in csvreader:
        votes.append(row[0])
        candidates.append(row[2])
total_votes = len(votes)

#creating a function that that will append unique name from list:
def unique(list): 
    for cand in list:
        if cand not in unique_cand:
            unique_cand.append(cand)
                
unique(candidates)

print(unique_cand)