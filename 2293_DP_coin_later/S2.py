import sys
from collections import defaultdict
input = sys.stdin.readline

def dfs(idx,target):
    global num_coin
    if target ==0:
        return 1
    # 이미 연산 해봤다면
    if dp[(idx,target)]>0:
        return dp[(idx,target)]
    elif dp[(idx,target)] == -1:
        return 0
    value = coin[idx]
    # 끝단까지 왔다면
    if idx == num_coin-1:
        if target%value == 0:
            dp[(idx,target)] = 1
            return 1
        dp[(idx,target)] = -1
        return 0
    # idx번째 수가 몇개까지 들어갈 수 있는가
    max_in = target//value
    ans = 0
    for j in range(max_in+1):
        if target-j*value == 0:
            ans+=1
        elif target - j*value >= coin[idx+1]:
            ans +=dfs(idx+1, target - j*value)
    if ans:
        dp[(idx,target)] = ans
    else:
        dp[((idx,target))] =-1
    return ans

coin = []
num_coin,target = map(int,input().split())
for i in range(num_coin):
    coin.append(int(input()))
coin.sort()
dp = defaultdict(int)
print(dfs(0,target))
