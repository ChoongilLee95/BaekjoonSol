import sys
num,jisu,num2  = map(int, sys.stdin.readline().strip().split())
stack_list = []
while jisu >1:
    if jisu%2 !=0:
        stack_list.append(1)
    stack_list.append(2)
    jisu //=2
num = num%num2
ans = num
while stack_list:
    a = stack_list.pop()
    if a ==2:
        ans =(ans**2)%num2
    else:
        ans= (ans*num)%num2
print(ans)
