import sys

M,N,L  = map(int,sys.stdin.readline().strip().split())

shooters  = list(map(int,sys.stdin.readline().strip().split()))
ans = 0
for i in range(N):
    x,y = map(int,sys.stdin.readline().strip().split())
    if y>L:
        continue
    else:
        for j in shooters:
            if abs(x-j)<L:
                if x > j:
                    if y+x-j-L<=0:
                        ans+=1
                        break
                else:
                    if y-x+j-L<=0:
                        ans +=1
                        break
print(ans)