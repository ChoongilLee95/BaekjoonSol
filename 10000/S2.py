import sys

n  = int(sys.stdin.readline().strip())
answer = 1
num_list = []
for _ in range(n):
    ans = 1
    a,b = map(int,sys.stdin.readline().strip().split())
    x1, x2 = a-b,a+b
    num_list.append([x1,x2,0])
num_list.sort(key=lambda x: (x[0], -x[1]))
print(num_list)
pl =0
for i in range(1,n):
    ans = 0
    pl_move =0
    for j in range(pl,i):
        if num_list[j][0] < num_list[i][0] <num_list[j][1] <num_list[i][1]:
            ans +=2
        

#     for i in num_list:
#         print(i,x1,x2)
#         if (x1-i[0])*(x1-i[1])*(x2-i[0])*(x2-i[1])<0:
#             ans +=2
#     print(ans)
#     num_list.append([x1,x2,0,0])
#     if ans==0:
#         ans = 1
#     answer +=ans
# print(answer)
