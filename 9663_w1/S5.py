import sys
input = sys.stdin.readline

# python
def bt(col):
    global ans
    # escape
    if col == n:
        ans += 1
        return

    for j in range(n if col else n//2):
        if not row[j] and not d1[col-j] and not d2[col+j]:
            row[j] = True
            d1[col-j] = True
            d2[col+j] = True

            bt(col+1)

            row[j] = False
            d1[col-j] = False
            d2[col+j] = False

n = int(input())
ans = 0

# python
# row
row = [False for _ in range(n)]
# right-down
d1 = [False for _ in range(n*2)]
# left-down
d2 = [False for _ in range(n*2)]
# odd n
bt(0)
ans *= 2
if n%2:
    # half * 2

    # mid
    m = n//2
    row[m] = d1[-m] = d2[m] = True
    bt(1)
print(ans)
## pypy
#def check(x):
#    for i in range(x):
#        if abs(row[x] - row[i]) == abs(x-i):
#            return False
#    return True
#
#def dfs(x):
#    global ans
#
#    if x == N:
#        ans += 1
#        return
#
#    else:
#        for i in range(N):
#            if not visited[i]:
#                row[x] = i
#
#                if check(x):
#                    visited[i] = True
#                    dfs(x+1)
#                    visited[i] = False


## pypy
#row = [0] * N
#visited = [False] * N
#dfs(0)
