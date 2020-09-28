#import modules
import csv
import os


#import the resource csv
election_csv = os.path.join("Resources","testcsv.csv")

#Variables
candidates = []
votes = []
unique_cand = []
vote_count = []
candidates_vote = []

#vote_gain = []
with open(election_csv,"r") as csvdata:
    csvreader = csv.reader(csvdata,delimiter=",")
    #skip header
    next(csvreader)
    
    for row in csvreader:
        votes.append(row[0])
        candidates.append(row[2])
        candidates_vote.count(candidates)
        


    for cand in candidates:
        if cand not in unique_cand:
            unique_cand.append(cand)
            
total_votes = len(votes)

vcount_0 = candidates.count(unique_cand[0])
per_0 = round((vcount_0/total_votes)*100,2)
vcount_1 = candidates.count(unique_cand[1])
per_1 = round((vcount_1/total_votes)*100,2)
vcount_2 = candidates.count(unique_cand[2])
per_2 = round((vcount_2/total_votes)*100,2)
vcount_3 = candidates.count(unique_cand[3])
per_3 = round((vcount_3/total_votes)*100,2)


print("Election Results \n")
print("----------------------------\n")
print(f'{unique_cand[0]} :{per_0}% ({vcount_0})')
print(f'{unique_cand[1]} :{per_1}% ({vcount_1})')
print(f'{unique_cand[2]} :{per_2}% ({vcount_2})')
print(f'{unique_cand[3]} :{per_3}% ({vcount_3})')
print("----------------------------")
print(f'Winner: {unique_cand[0]}')
print("----------------------------\n")

