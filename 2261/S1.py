import sys
ax_list = []
n  = int(sys.stdin.readline().strip())
x,y  = map(int,sys.stdin.readline().strip().split())
ax_list.append([x,y])
a,b  = map(int,sys.stdin.readline().strip().split())
ax_list.append([a,b])
ans = (x-a)**2 + (b-y)**2
for _ in range(n-2):
    x,y  = map(int,sys.stdin.readline().strip().split())
    for i in ax_list:
        a = (x-i[0])**2 + (y-i[1])**2
        if a==0:
            break
        if a < ans:
            ans = a
    else:
        ax_list.append([x,y])
print(ans)

