# Trading profits/losses data
trading_pnl = [-224, 352, 252, 354, -544, -650, 56, 123, -43, 254, 325, -123, 47, 321, 123, 133, -151, 613, 232, -311]

# Initialize metrics
total_days = len(trading_pnl)
total_pnl = sum(trading_pnl)
profitable_days = []
unprofitable_days = []

# Initialize best_gain and worst_loss
best_gain = trading_pnl[0]
worst_loss = trading_pnl[0]

# Iterate over trading_pnl
for day_pnl in trading_pnl:
    # Classify days as profitable or unprofitable
    if day_pnl > 0:
        profitable_days.append(day_pnl)
        # Check if current day's profit is greater than best_gain
        if day_pnl > best_gain:
            best_gain = day_pnl
    elif day_pnl <= 0:
        unprofitable_days.append(day_pnl)
        # Check if current day's loss is less than worst_loss
        if day_pnl < worst_loss:
            worst_loss = day_pnl

# Calculate metrics
num_profit_days = len(profitable_days)
num_unprofit_days = len(unprofitable_days)
avg_daily_pnl = total_pnl / total_days
percent_profit_days = (num_profit_days / total_days) * 100
percent_unprofit_days = (num_unprofit_days / total_days) * 100

# Print results
print(f"Number of total trading days: {total_days}")
print(f"Total profits and losses: {total_pnl}")
print(f"Daily average profit and loss: {avg_daily_pnl}")
print(f"Worst loss: {worst_loss}")
print(f"Best gain: {best_gain}")
print(f"Number of profitable days: {num_profit_days}")
print(f"Number of unprofitable days: {num_unprofit_days}")
print(f"Percentage of profitable days: {percent_profit_days}%")
print(f"Percentage of unprofitable days: {percent_unprofit_days}%")
print("Profitable days:", profitable_days)
print("Unprofitable days:", unprofitable_days)