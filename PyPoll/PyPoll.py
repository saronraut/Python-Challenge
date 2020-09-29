#scripts was created using external resources such as geekforgeek.org and stackoverflow
# Class Activity examples were used to build to script as well.  

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
    
    #create a loop to read the rows in the csv and append the value in a list
    for row in csvreader:
        votes.append(row[2])
        candidates.append(row[2])
         
    #for loop to find unique name to indentify the candidates    
    for cand in candidates:
        if cand not in unique_cand:
            unique_cand.append(cand)

#creating a function that that loops through the name of candidates in row 2 to find the most reoccuring name.
# the function was created using resources from https://www.geeksforgeeks.org/python-find-most-frequent-element-in-a-list/
def most_count(list):
    counter = 0 
    cand_name = list[0]
#this will give me the name of the candidates that recieved the most amouhnt of votes. 
    for cand_name in list: 
        curr_most = list.count(cand_name)
        if (curr_most > counter):
            counter = curr_most
            curr_most = cand_name
        return curr_most

# Winner is the name that occured the most in candidates list, hence received the most vote        
winner = (most_count(candidates))

 #total vote casted according to the csv.        
total_votes = len(votes)

#calculate the values for each unique candidates from unqiue candidate list: unique_candiate =[Khan, Correy, Li, O'Tooley]
# Khan is 0 on the list
vcount_0 = candidates.count(unique_cand[0])
per_0 = round((vcount_0/total_votes)*100,2)

#Correy is 1 on the list
vcount_1 = candidates.count(unique_cand[1])
per_1 = round((vcount_1/total_votes)*100,2)

#Li is 2 on the list 
vcount_2 = candidates.count(unique_cand[2])
per_2 = round((vcount_2/total_votes)*100,2)

#O'Tooley is 3 on the list
vcount_3 = candidates.count(unique_cand[3])
per_3 = round((vcount_3/total_votes)*100,2)

#print out the data on each candidates
print("Election Results \n")
print("----------------------------\n")
print(f'{unique_cand[0]} : {per_0}% ({vcount_0})')
print(f'{unique_cand[1]} : {per_1}% ({vcount_1})')
print(f'{unique_cand[2]} : {per_2}% ({vcount_2})')
print(f'{unique_cand[3]} : {per_3}% ({vcount_3})')
print("----------------------------")
print(f'Winner: {winner}')
print("----------------------------\n")

#create an output on a txt file
output_path = os.path.join("pypoll.txt")
with open('pypoll.txt' , 'w') as file:
    file.write("Election Results \n")
    file.write("----------------------------\n")
    file.write(f'{unique_cand[0]} : {per_0}% ({vcount_0}) \n' )
    file.write(f'{unique_cand[1]} : {per_1}% ({vcount_1})\n')
    file.write(f'{unique_cand[2]} : {per_2}% ({vcount_2})\n')
    file.write(f'{unique_cand[3]} : {per_3}% ({vcount_3})\n')
    file.write("---------------------------- \n")
    file.write(f'Winner: {winner} \n')
    file.write("----------------------------\n")
file.close

