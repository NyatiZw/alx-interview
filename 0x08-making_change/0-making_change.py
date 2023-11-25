#!/usr/bin/python3
"""
Function to determine fewest number of coins needed to meet total

Attributes:
    - coins: List of values of coins
    - total: integer value of coins

Returns:
    Total or 0
"""


def makeChange(coins, total):
    # If total is 0 oe less, return 0
    if total <= 0:
        return 0

    # Initialize an array to store the minimum number of coins
    dp = [float('inf')] * (total + 1)

    # Base case: 0 coins needed for total 0
    dp[0] = 0

    # Iterate through each coin value
    for coin in coins:
        # Update dp array for each possible total
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    # if total can not be met by any number
    if dp[total] == float('inf'):
        return -1

    # Return the minimum number of coins needed
    return dp[total]
