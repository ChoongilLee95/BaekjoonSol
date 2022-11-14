import sys

input  = sys.stdin.readline

N , M = map(int,input().strip().split())
target = N//2

rel_small = [[] for _ in range(N+1)]
rel_big = [[] for _ in range(N+1)]
for _ in range(M):
    new = list(map(int, input().strip().split()))
    rel_big[new[1]].append(new)
    rel_small[new[0]].append(new)

def dfs_small(n):
    global len_small
    len_small+=1
    for i in rel_big[n]:
        dfs_small(i[0])
def dfs_big(n):
    global len_big
    len_big+=1
    for i in rel_small[n]:
        dfs_big(i[1])
def dfs_bigger(n):
    if because_big[n]:
        because_big[n] = False
        for i in rel_small[n]:
            dfs_bigger(i[1])
def dfs_smaller(n):
    if because_big[n]:
        because_big[n] = False
        for i in rel_small[n]:
            dfs_bigger(i[1])
ans = 0
because_big = [True]*(N+1)
because_small = [True]*(N+1)
for i in range(1,N+1):
    if because_small[i] and because_big[i]:
        len_small = 0
        len_big = 0
        for j in rel_big[i]:
            dfs_small(j[0])
        if len_small > target:
            ans +=1
            because_big[i] = False
            for j in rel_small[i]:
                dfs_bigger(j[1])
        else:
            for j in rel_small[i]:
                dfs_big(j[0])
            if len_big > target:
                ans +=1
                because_small[i] = False
                for j in rel_big[i]:
                    dfs_smaller(j[0])
    else:
        ans +=1
print(ans)

