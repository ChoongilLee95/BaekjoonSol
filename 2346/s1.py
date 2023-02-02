import sys

input = sys.stdin.readline

N = int(input())

num_b = list(map(int, input().strip().split()))

check = [0]*N

check[0] = 1
start = 0
ans = [1]
for _ in range (N-1):
    move = num_b[start]
    if move > 0:
        while move != 0:
            start+=1
            if start >N-1:
                start = 0
            while check[start]==1:
                start+=1
                if start > N-1:
                    start = 0
            move-=1
    else:
        while move !=0:
            start -=1
            if start <0:
                start = N-1
            while check[start] ==1:
                start -=1
                if start <0:
                    start = N-1
            move +=1
    check[start] = 1
    ans.append(start+1)

print(*ans)

        
