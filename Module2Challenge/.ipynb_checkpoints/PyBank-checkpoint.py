import csv
from pathlib import Path

# Define the path to the budget_data.csv
budget_data_filepath = Path('C:/Users/jan/Desktop/FinTech/Module2Challenge/PyBank/Resources/budget_data.csv')

# Initialize variables
total_months = 0
total_profit_loss = 0
previous_month_profit_loss = 0
monthly_change = []
greatest_increase = ["", 0]
greatest_decrease = ["", float('inf')]

# Read the CSV file
with open(budget_data_filepath, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader)

    # Loop through the rows in the CSV
    for row in csvreader:
        # Count the total number of months
        total_months += 1

        # Calculate the total profit/loss
        current_month_profit_loss = int(row[1])
        total_profit_loss += current_month_profit_loss

        # Calculate the monthly change in profit/loss
        if total_months > 1:
            change = current_month_profit_loss - previous_month_profit_loss
            monthly_change.append(change)

            # Check for greatest increase in profits
            if change > greatest_increase[1]:
                greatest_increase[0] = row[0]
                greatest_increase[1] = change

            # Check for greatest decrease in losses
            if change < greatest_decrease[1]:
                greatest_decrease[0] = row[0]
                greatest_decrease[1] = change

        # Update the previous month's profit/loss
        previous_month_profit_loss = current_month_profit_loss

# Calculate the average change in profit/loss
average_change = sum(monthly_change) / len(monthly_change)

# Print the analysis
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_profit_loss}")
print(f"Average  Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})")
print(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})")

# Write the analysis to a text file
output_path = Path('financial_analysis.txt')
with open(output_path, 'w') as file:
    file.write("Financial Analysis\n")
    file.write("----------------------------\n")
    file.write(f"Total Months: {total_months}\n")
    file.write(f"Total: ${total_profit_loss}\n")
    file.write(f"Average  Change: ${average_change:.2f}\n")
    file.write(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n")
    file.write(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")
