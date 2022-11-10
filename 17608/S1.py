import sys

n  = int(sys.stdin.readline().strip())

nums =[]
nums.append(int(sys.stdin.readline().strip()))
for i in range(n-1):
    num = int(sys.stdin.readline().strip())
    while nums[-1] <=num:
        nums.pop()
        if len(nums)==0:
            break
    nums.append(num)
print(nums)
print(len(nums))

