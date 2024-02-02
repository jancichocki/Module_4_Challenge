# Initialize dictionary of banks and market caps
banks = {
    "JP Morgan Chase": 327,
    "Bank of America": 302,
    "Citigroup": 173,
    "Wells Fargo": 273,
    "Goldman Sachs": 87,
    "Morgan Stanley": 72,
    "U.S. Bancorp": 83,
    "TD Bank": 108,
    "PNC Financial Services": 67,
    "Capital One": 47,
    "FNB Corporation": 4,
    "First Hawaiian Bank": 3,
    "Ally Financial": 12,
    "Wachovia": 145,
    "Republic Bancorp": 0.97
}

# Change Citigroup's market cap
banks["Citigroup"] = 170

# Add American Express to the dictionary
banks["American Express"] = 33

# Remove Wachovia from the dictionary
del banks["Wachovia"]

# Initialize metrics and lists for different tiers of banks
total_market_cap = 0
num_banks = 0
mega_cap = []
large_cap = []
mid_cap = []
small_cap = []

# Iterate over banks dictionary
for bank_name, market_cap in banks.items():
    # Calculate total market cap
    total_market_cap += market_cap
    # Increment number of banks
    num_banks += 1
    # Group banks by tiers based on their market cap
    if market_cap >= 300:
        mega_cap.append(bank_name)
    elif market_cap >= 10:
        large_cap.append(bank_name)
    elif market_cap >= 2:
        mid_cap.append(bank_name)
    else:
        small_cap.append(bank_name)

# Calculate average market cap
avg_market_cap = total_market_cap / num_banks

# Find the largest and smallest bank
largest_bank = max(banks, key=banks.get)
smallest_bank = min(banks, key=banks.get)

# Print results
print(f"Total Market Capitalization: {total_market_cap}")
print(f"Total Number of Banks: {num_banks}")
print(f"Average Market Capitalization: {avg_market_cap:.2f}")
print(f"Largest Bank: {largest_bank}")
print(f"Smallest Bank: {smallest_bank}")
print("------------------------------------------------")
print(f"Mega Cap Banks: {mega_cap}")
print(f"Large Cap Banks: {large_cap}")
print(f"Mid Cap Banks: {mid_cap}")
print(f"Small Cap Banks: {small_cap}")