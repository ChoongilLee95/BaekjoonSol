import sys

x,y  = map(int,sys.stdin.readline().strip().split())

num_axis = int(sys.stdin.readline().strip())
x_axis = [0,y]
y_axis = [0,x]
for cut in range(num_axis):
    a,b  = map(int,sys.stdin.readline().strip().split())
    if a == 0:
        x_axis.append(b)
    else:
        y_axis.append(b)
y_ans = 0
x_ans = 0
x_axis.sort()
y_axis.sort()

for i in range(len(x_axis)-1):
    a = x_axis[i+1]-x_axis[i]
    if a >x_ans:
        x_ans =a

for i in range(len(y_axis)-1):
    a = y_axis[i+1]-y_axis[i]
    if a >y_ans:
        y_ans =a
ans = x_ans*y_ans
print(ans)

