
## 병휘형님 sol
## 포커스, 재귀를 통해 뻗어나가는 생각

import sys
input = sys.stdin.readline

b = [1, 2, 3]

def dfs(s, n):
    global ret
    if n == s:
        ret += 1 
        return 
    if n < s: return 
    for i in b: 
        dfs(s+i, n)
    return

for _ in range(int(input())):
    n = int(input())
    ret = 0
    dfs(0, n)
    print(ret)