originalPrice = 360.35
currentPrice = 293.33
tBuy = -20
tSell = 20
balance = 1000

increase = currentPrice - originalPrice
percentIncrease = (increase / originalPrice) * 100

# Determine recommendation
recommendation = "hold"
if percentIncrease <= tBuy and balance >= currentPrice * 5:
    recommendation = "buy"
elif percentIncrease >= tSell:
    recommendation = "sell"

# Print original price, current price, percent increase, and recommendation
print(f"Original Price: ${originalPrice}")
print(f"Current Price: ${currentPrice}")
print(f"Percent Increase: {percentIncrease:.2f}%")
print(f"Recommendation: {recommendation}")