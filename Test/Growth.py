# Global list to store growth rates
growth_rates = []

# Function to calculate compound growth rate
def calculate_compound_growth_rate(beginning_balance, ending_balance, years):
    growth_rate = ((ending_balance / beginning_balance) ** (1 / years)) - 1
    growth_rates.append(growth_rate)
    return growth_rate

# Year 2016
beginning_balance = 29000.00
ending_balance = 45000.10
years = 1.0
calculate_compound_growth_rate(beginning_balance, ending_balance, years)

# Year 2017
beginning_balance = 45000.00
ending_balance = 47000.00
calculate_compound_growth_rate(beginning_balance, ending_balance, years)

# Year 2018
beginning_balance = 47000.00
ending_balance = 48930.00
calculate_compound_growth_rate(beginning_balance, ending_balance, years)

# Round and print the growth rates
year_one_growth = round(growth_rates[0] * 100, 2)
year_two_growth = round(growth_rates[1] * 100, 2)
year_three_growth = round(growth_rates[2] * 100, 2)

print(f"Year One Growth: {year_one_growth}%")
print(f"Year Two Growth: {year_two_growth}%")
print(f"Year Three Growth: {year_three_growth}%")

# Print all growth rates
print("Growth rates: ", [round(rate * 100, 2) for rate in growth_rates])
