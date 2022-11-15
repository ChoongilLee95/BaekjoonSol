
import sys
input = sys.stdin.readline
num_coin, target = map(int,input().strip().split())

coin = []
for _ in range(num_coin):
    coin.append(int(input()))

def dfs(target):
    if target==0:
        return 1
    ans = 0
    for i in coin:
        if target-i>=0:
            ans += dfs(target-i)
    return ans