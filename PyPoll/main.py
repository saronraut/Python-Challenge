#import modules
import csv
import os


#import the resource csv
election_csv = os.path.join("Resources","election_data.csv")


#Set of assigned variables that will store the data as a list 
candidates = []
votes = []
unique_cand = []


#open csv to read the data, assign delimiter to seperate rows
with open(election_csv,"r") as csvdata:
    csvreader = csv.reader(csvdata,delimiter=",")
    #skips header 
    next(csvreader)
    
    #create a loop to read the rows in the csv 
    for row in csvreader:
        votes.append(row[0])
        candidates.append(row[2])
       
    #find unique name to indentify the candidates    
    for cand in candidates:
        if cand not in unique_cand:
            unique_cand.append(cand)

 #total vote casted according to the csv.        
total_votes = len(votes)

#calculate the values for each unique candidates from unqiue candidate list [Khan, Correy, Li, O'Tooley]
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
print(f'{unique_cand[0]} : {per_0}% ({vcount_0})')
print(f'{unique_cand[1]} : {per_1}% ({vcount_1})')
print(f'{unique_cand[2]} : {per_2}% ({vcount_2})')
print(f'{unique_cand[3]} : {per_3}% ({vcount_3})')
print("----------------------------")
print(f'Winner: {unique_cand[0]}')
print("----------------------------\n")