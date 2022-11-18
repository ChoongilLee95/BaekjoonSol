

num_coin, t = map(int,input().split())
coins =[]
for _ in range(num_coin):
    coins.append(int(input()))
dp = [0] * (t + 1)
dp[0] = 1
for coin in coins:
    for i in range(1, t + 1):
        if i < coin: continue
        dp[i] += dp[i - coin]
print(dp[t])