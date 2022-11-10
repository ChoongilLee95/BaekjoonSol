import sys

n = int(sys.stdin.readline().strip())

nums = list(map(int,sys.stdin.readline().strip().split()))

stack = []
ans = []
for i in range(n):
    if i ==0:
        ans.append(0)
        stack.append([nums[i],1])
    else:
        while len(stack)!=0 and stack[-1][0]<=nums[i]:
            stack.pop()
        if len(stack):
            ans.append(stack[-1][1])
        else:
            ans.append(0)
        stack.append([nums[i],i+1])
print(*ans)