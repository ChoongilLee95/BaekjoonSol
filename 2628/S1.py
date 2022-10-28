import sys
def cha(t,k):
    ans = t-k
    if ans<0:
        ans =-ans
    return ans

x,y  = map(int,sys.stdin.readline().strip().split())

num_axis = int(sys.stdin.readline().strip())
x_axis = [0,x]
y_axis = [0,y]
for cut in range(num_axis):
    a,b  = map(int,sys.stdin.readline().strip().split())
    if a == 0:
        x_axis.append(b)
    else:
        y_axis.append(b)
y_ans = 0
x_ans = 0
for i in range(len(x_axis)):
    for j in range(i+1,len(x_axis)):
        a = cha(x_axis[i],x_axis[j])
        if a >x_ans:
            x_ans =a

for i in range(len(y_axis)):
    for j in range(i+1,len(y_axis)):
        a = cha(y_axis[i],y_axis[j])
        if a >y_ans:
            y_ans =a
ans = x_ans*y_ans
print(ans)

