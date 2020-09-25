#import modules
import csv
import os

#import the resource csv
budget_csv = os.path.join("Resources","budget_data.csv")

#create variables for list
months = []
prof_loss = []

      
#open the csv file
with open(budget_csv,"r") as csvdata:
    csvreader = csv.reader(csvdata,delimiter=",")
    #to skip the header
    next(csvreader)
    #creating a for loops to get the month and changes from the csv as a list
    for row in csvreader:
        months.append(row[0])
        prof_loss.append(int(row[1]))
       
      
#using the len() calculate the total of month in dataset
total_month = len(months)
print(f'Total Months: {total_month}')

# #using sum()create the total
total_profloss = sum(prof_loss)
print(f'Total profit/loss: ${total_profloss}')
 
#Analysis

prof_loss = []
def avg(bank_data):
    total = 0
    t_numb = len(bank_data)
    for numb in bank_data:
        total = total + numb
    average = total/t_numb
    print(avg)
    return avg

avg(prof_loss)





    
    
    



#use max()to find the greatest increase in profit..

#needs to get data for month and amount


#use min()to find the greatest decrease in profit..
#needs to get data for month and amount


#use print to display the data

#export the data on csv
