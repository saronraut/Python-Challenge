#scripts was created using external resources such as geekforgeek.org and stackoverflow
# Class Activity examples were used to build to script as well.  

#import modules
import csv
import os

#import the resource csv
budget_csv = os.path.join("Resources","budget_data.csv")

#create variables for list
months = []
prof_loss = []
monthly_change = []
  
#open the csv file
with open(budget_csv,"r") as csvdata:
    csvreader = csv.reader(csvdata,delimiter=",")
    #to skip the header
    next(csvreader)
    #creating for loops to get the month and changes from the csv as a list
    for row in csvreader:
        months.append(row[0])
        prof_loss.append(int(row[1]))

 #to get the average change between each month       
    for col in range(len(prof_loss)-1):
        monthly_change.append(prof_loss[col+1] - prof_loss[col])

#Average change for the period
avg = round(sum(monthly_change)/len(monthly_change),2)

#using the values in monthly_change identify the increase and decrease
#+1 for month because it will be for next month since doing average
max_inc = max(monthly_change)
max_month = months[monthly_change.index(max_inc)+ 1]

min_dec = min(monthly_change)
min_month = months[monthly_change.index(min_dec)+ 1]
         
#using the len() calculate the total of month in dataset
total_month = len(months)

# #using sum()create the sum total profit/loss value
total_profloss = sum(prof_loss)

#Print Data
print('Financial Analysis')
print("---------------------------- \n")
print(f'Total Months: {total_month}')
print(f'Total profit/loss: ${total_profloss}')
print(f'Average Change: {avg}')
print(f'Greatest Increase in Profits: {max_month} (${max_inc})')
print(f'Greatest Decrease in Profits: {min_month} (${min_dec}')
    
#create an output for txt file
output_path = os.path.join("pybank.txt")
with open('pybank.txt','w') as file: 
    file.write('Financial Analysis')
    file.write("---------------------------- \n")
    file.write(f'Total Months: {total_month}\n')
    file.write(f'Total profit/loss: ${total_profloss}\n')
    file.write(f'Average Change: {avg}\n')
    file.write(f'Greatest Increase in Profits: {max_month} (${max_inc})\n')
    file.write(f'Greatest Decrease in Profits: {min_month} (${min_dec}\n')
file.close