import sys
input = sys.stdin.readline


## 메모이제이션 사용 가능 
dp = [1] * 10004
dp[1] = 0
deci = []
for i in range(2, 10001):
    if dp[i]:
        deci.append(i)
        for j in range(i*2, 10001, i):
            dp[j] = 0
for _ in range(int(input())):
    n = int(input())
    l = [0, 0]
    for i in deci:
        if i >= n // 2 + 1:
            break
        if dp[n - i]:
            l[0] = i
            l[1] = n - i
    print(*l, sep=' ')