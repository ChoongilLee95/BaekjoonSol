import sys
def squr(n):
    new = []
    for col in range(n):
        new_col = []
        for row in range(n):
            new_col.append(find_num(n,col,row))
        new.append(new_col)
    return new
def find_num(n,c,r):
    answer = 0
    for i in range(n):
        answer += ans[c][i]*ans[i][r]
    return answer%1000

def multi(n):
    new = []
    for col in range(n):
        new_col = []
        for row in range(n):
            new_col.append(find_num2(n,col,row))
        new.append(new_col)
    return new
def find_num2(n,c,r):
    answer = 0
    for i in range(n):
        answer += now[c][i]*ans[i][r]
    return answer%1000

n,jisu  = map(int, sys.stdin.readline().strip().split())
now = []
for _ in range(n):
    now.append(list(map(int, sys.stdin.readline().strip().split())))
stack_list = []
while jisu >1:
    if jisu%2 !=0:
        stack_list.append(1)
    stack_list.append(2)
    jisu //=2

ans = now
while stack_list:
    a = stack_list.pop()
    if a ==2:
        ans = squr(n)
    else:
        ans= multi(n)
for i in ans:
    a = ''
    for j in i:
        a +=f'{j%1000} '
    print(a.strip())
