import sys

input  = sys.stdin.readline

num_stuff,w_max = map(int,input().split())

stuff = []

for _ in range(num_stuff):
    w,v = map(int, input().split())
    stuff.append((w,v))
dp = [0]*(w_max+1)

for d_w in range(w_max):
    d_v = dp[d_w]
    for n_w,n_v in stuff:
        if d_w + n_w > w_max:
            continue
        if d_v+n_v > dp[d_w+n_w]:
            dp[d_w+n_w] = d_v+n_v
print(dp[w_max])
