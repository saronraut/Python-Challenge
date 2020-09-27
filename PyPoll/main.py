#import modules
import csv
import os


#import the resource csv
election_csv = os.path.join("Resources","election_data.csv")

with open(election_csv,"r") as csvdata:
    csvreader = csv.reader(csvdata,delimiter=",")

candidates = []

# pull out the list of candidates
    for row in csvreader:
        total_candidates(row[2])

print(candidates)
