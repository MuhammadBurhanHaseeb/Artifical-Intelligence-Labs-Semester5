def min_coin_change_recursive(coins, target):
    if target == 0:
        return 0

    min_count = float('inf')

    for coin in coins:
        if target - coin >= 0:
            count = min_coin_change_recursive(coins, target - coin)
            if count != -1:
                min_count = min(min_count, count + 1)

    return min_count if min_count != float('inf') else -1

def min_coin_change(coins, target):
    dp = [float('inf')] * (target + 1)
    dp[0] = 0

    for coin in coins:
        for amount in range(coin, target + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    return dp[target]

coin_denominations = [7, 9, 2]
target_amount = 11

min_coins_recursive = min_coin_change_recursive(coin_denominations, target_amount)
min_coins_dynamic = min_coin_change(coin_denominations, target_amount)

print("Minimum number of coins required (Recursive):", min_coins_recursive)
print("Minimum number of coins required (Dynamic Programming):", min_coins_dynamic)
