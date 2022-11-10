import sys

n  = int(sys.stdin.readline().strip())
answer = 1
num_list = []
for _ in range(n):
    ans = 1
    a,b = map(int,sys.stdin.readline().strip().split())
    x1, x2 = a-b,a+b
    for i in num_list:
        print(i,x1,x2)
        if (x1-i[0])*(x1-i[1])*(x2-i[0])*(x2-i[1])<0:
            ans +=2
    print(ans)
    num_list.append([x1,x2,0,0])
    if ans==0:
        ans = 1
    answer +=ans
print(answer)
