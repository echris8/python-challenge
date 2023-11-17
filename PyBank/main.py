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
input_path = os.path.join(os.path.dirname(__file__), "Resources", "budget_data.csv") 

with open(input_path, 'r') as csvfile: 
    csvreader = csv.reader(csvfile)
    header = next(csvreader)

    #Find number of months and net profit 
    for row in csvreader: 

        months = months+1
        profit_loss=int(row[1])
        net_total = net_total+profit_loss

        #Find net change 
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

#Identify file to write to 
output_path = os.path.join(os.path.dirname(__file__), "analysis.md")

#Write results to the file 
with open(output_path, "w") as md_file:
    md_file.write("Financial Analysis\n")
    md_file.write("-" * 28 + "\n")
    md_file.write(f"Total Months: {int(months)}\n")
    md_file.write(f"Total: ${int(net_total)}\n")
    md_file.write(f"Average Change: ${(average_change)}\n")
    md_file.write(f"Greatest Increase in Profits: {greatest_increase_date} (${int(greatest_increase)})\n")
    md_file.write(f"Greatest Decrease in Profits: {greatest_decrease_date} (${int(greatest_decrease)})\n")
#Print

#Print results 
print(f"Results written to {output_path}") 