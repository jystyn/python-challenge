import csv
import os

#relative path to data file python-challenge/PyBank/Resources/budget_data.csv
bank_data_csv = os.path.join("Python_Starter","python-challenge","PyBank", "Resources", "budget_data.csv")

#create list to store data
budget_data = []

#this loop goes through data to store in dictionary
with open(bank_data_csv) as csvfile:
    reader=csv.DictReader(csvfile)

    for row in reader:
        budget_data.append({"Month": row["Date"], "Amount": int(row["Profit/Losses"]), "Change": 0})

#the total number of months in dataset
total_months = len(budget_data)
#print(total_months)

#this loop allows us to calculate the Change for each index
prev_amount = budget_data[0]["Amount"]
for i in range(total_months):
    budget_data[i]["Change"] = budget_data[i]['Amount'] - prev_amount
    prev_amount = budget_data[i]["Amount"]
#print(budget_data)
    
#the net total of all "Profit/Losses" over the entire period    
net_total = sum(row["Amount"] for row in budget_data)
#print(net_total)

#the changes in "Profit/Losses" over th entire period, and then the average of those changes
total_row_change = sum(row["Change"] for row in budget_data)
average = round(total_row_change/(total_months - 1), 2)
#print(total_row_change)
#print(average)

#the greatest increase in profits(date and amount) over the entire period
max_increase = max(budget_data, key = lambda x:x["Change"])
#print(max_increase)

#the greatest decrease in profits(date and amount) over the entire period 
max_decrease = min(budget_data, key = lambda x:x["Change"])
#print(max_decrease)

#print(f'Total Months: {total_months}')
#print(f'Total: {net_total}')
#print(f'Average Change: {average}')
#print(f'Greastest Increase in Profits: {max_increase["Month"]} ${max_increase["Change"]}')
#print(f'Greastest Decrease in Profits: {max_decrease["Month"]} ${max_decrease["Change"]}')

txt_output = (
    f'Financial Analysis\n'
    f'----------------------------\n'
    f'Total Months: {total_months}\n'
    f'Total: ${net_total}\n'
    f'Average Change: ${average}\n'
    f'Greastest Increase in Profits: {max_increase["Month"]} ${max_increase["Change"]}\n'
    f'Greastest Decrease in Profits: {max_decrease["Month"]} ${max_decrease["Change"]}\n'
) 

print(txt_output)

new_file = "python-challenge/PyBank/Analysis/result.txt"

with open(new_file, "w") as f:
    f.write(txt_output)