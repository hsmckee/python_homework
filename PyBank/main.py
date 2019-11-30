import os
filepath = os.path.join ("data","budget_data.csv")
#Calculating Total Months
filename = "budget_data.csv"
header_key = "Date"

#Average of the changes in "Profit/Losses" over the entire period
#calculate changes
months = []
profit_losses = []
changes = []

with open (filename) as f:
    for line in f:
        (m, pl) = line.split(',')
        
#ignoring top line
        if header_key not in m:      
            pl=int(pl)
            months.append (m)
            profit_losses.append(pl)
            
# Calculating the changes
    for num in range (1, len(profit_losses)):
        changes.append (profit_losses[num]-profit_losses[num-1])
average_changes = (sum(changes)/len(changes))
total_months = len(months)
#Output
print ("Financial Analysis")
print ("-------------------------------")
print (f'Total Months: {total_months}')

total_pl = sum(profit_losses)
print (f'Total: ${total_pl}')

print (f'Average Changes: ${average_changes:.2f}') 

#greatest increase in profits
max_increase = max(changes)
index_max = changes.index(max_increase)
max_month = months[index_max + 1 ]
print (f'Greatest Increase in Profits: {max_month} (${max_increase})')

#greatest decrease in profits
decrease = min(changes)
index_min = changes.index(decrease)
min_month = months[index_min + 1 ]
print (f'Greatest Decrease in Profits: {min_month} (${decrease})')




