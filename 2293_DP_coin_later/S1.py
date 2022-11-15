import sys
input = sys.stdin.readline
num_coin, target = map(int,input().strip().split())

coin = []
for _ in range(num_coin):
    coin.append(int(input()))
coin.sort()
end = len(coin)-1
def dfs(idx,target):
    if idx == end:
        if target%coin[idx] == 0:
            return 1
        else:
            return 0
    ans = 0
    free = (target-coin[idx+1])//coin[idx]
    if target%coin[idx] == 0:
        ans+=1
    for i in range(free+1):
        ans += dfs(idx+1,target-i*coin[idx])
    return ans
print(dfs(0,target))