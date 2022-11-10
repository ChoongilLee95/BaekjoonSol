import sys

n  = int(sys.stdin.readline().strip())
nums = []
for i in range(n):
    num  = int(sys.stdin.readline().strip())
    if num:
        nums.append(num)
    else:
        nums.pop()
print(sum(nums))


