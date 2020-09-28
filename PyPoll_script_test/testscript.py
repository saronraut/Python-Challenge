#import modules
import csv
import os


#import the resource csv
election_csv = os.path.join("Resources","testcsv.csv")

#Variables
candidates = []
votes = []
unique_cand = []


#vote_gain = []
with open(election_csv,"r") as csvdata:
    csvreader = csv.reader(csvdata,delimiter=",")
    #skip header
    next(csvreader)
    
    for row in csvreader:
        votes.append(row[0])
        candidates.append(row[2])


for cand in candidates:
    if cand not in unique_cand:
        unique_cand.append(cand)
            
total_votes = len(votes)

# count_0 = candidates.count(unique_cand[0])
# count_1 = candidates.count(unique_cand[1])
# count_2 = candidates.count(unique_cand[2])
# count_3 = candidates.count(unique_cand[3])









