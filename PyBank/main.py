#Declare variables
import os
import csv 

months = 0
profit_list = []
net_total = 0
greatest_increase = 0
greatest_increase_date = ""
greatest_decrease = 0
greatest_decrease_date = ""

#Tie to resources csv file 
csvpath = os.path.reader('Resources''budget_data.csv')

#Find total number months
with open(csvpath, 'r') as csvfile: 
    csvreader = csv.reader(csvfile)
    header = next(csvreader)

    for row in csvreader: 

        months = months+1
        profit_loss=int(row[1])
        net_total = net_total+profit_loss

        if months > 1 : 
            net_change = profit_loss - previous_profit_loss
            profit_list.append(net_change)

            #Find greatest increase and decrease in profits
            if net_change > greatest_increase:
                greatest_increase = net_change 
                greatest_increase_date = row[0]

            if net_change < greatest_decrease:
                greatest_decrease = net_change
                greatest_decrease_date = row[0]


        previous_profit_loss = profit_loss 

    average_change = sum(profit_list)/len(profit_list)

#Print results 
