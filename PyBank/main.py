import csv
import os

csvpath = os.path.join('Resources','budget_data.csv')

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    # Skip the header 
    next(csvreader)
    
    # Definitions 
    total_months = 0
    total_profit = 0
    prev_profit = 0
    changes_sum = 0
    max_change = 0
    min_change = 0
    max_change_month = "date"
    min_change_month = "date"
    
    # Begin looping through the rows of data
    for row in csvreader:
        if total_months == 0:
            # each iteration we add 1 to the total number of months
            total_months += 1
            # each itteration we add the profit/loss to the total
            total_profit += int(row[1])
            #set the variable to be used as previous month's profit in the net loop
            prev_profit = int(row[1])
        else:
            # each iteration we add 1 to the total number of months
            total_months += 1
            # each itteration we add the profit/loss to the total
            total_profit += int(row[1])
            # define the change to be this month's profit minus the prior month's
            change = (int(row[1])-prev_profit)
            # add up each change in profit so we can find the average
            changes_sum += change
            #set the variable to be used as previous month's profit in the net loop
            prev_profit = int(row[1])
        
            # to find min/max change, redefine the min/max variable if the current loop's change is less/greater
            if change > max_change:
                max_change = change
                max_change_month = str(row[0])
            if change < min_change:
                min_change = change
                min_change_month = str(row[0])    
    
    # Output:
    print('Financial Analysis')
    print('---------------------------------------------------')
    
    #The total number of months included in the dataset
    print(f'Total Months: {total_months}')
    
    #The net total amount of "Profit/Losses" over the entire period
    print(f'Total: ${total_profit:,d}')
    
    #The average of the changes in "Profit/Losses" over the entire period
    average_change = changes_sum / (total_months-1)
    print(f'Average Change: ${average_change:,.2f}') 
    
    #The greatest increase in profits (date and amount) over the entire period
    print(f'Greatest Increase in Profits: {max_change_month} (${max_change:,})')
    
    #The greatest decrease in losses (date and amount) over the entire period
    print(f'Greatest Decrease in Profits: {min_change_month} (${min_change:,})')


# save the output file path
output_path = os.path.join('PyBank.txt')

# open the output file, create a header row, and then write the zipped object to the csv
with open(output_path, 'w') as output:
    writer = csv.writer(output)
    
    writer.writerow(['Financial Analysis'])
    writer.writerow(['------------------------------------------'])
    writer.writerow(['Total Months:', total_months])
    writer.writerow(['Total:', total_profit])
    writer.writerow(['Average Change:',average_change])
    writer.writerow(['Greatest Increase in Profits:', max_change_month, max_change])
    writer.writerow(['Greatest Decrease in Profits:', min_change_month, min_change])
    
    output.close()