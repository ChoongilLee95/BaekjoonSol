import sys

input  = sys.stdin.readline

num_stuff,w_max = map(int,input().split())

stuff = []

for _ in range(num_stuff):
    w,v = map(int, input().split())
    stuff.append((w,v))
dp = [0]*(w_max+1)

for n_w,n_v in stuff:
    for idx in range(w_max-n_w,-1,-1):
        if dp[idx+n_w] < dp[idx] +n_v:
            dp[idx+n_w] = dp[idx] +n_v

print(dp[w_max])
