import sys
nums, re = map(int, sys.stdin.readline().split(' '))
test_nums = list(map(int, sys.stdin.readline().split(' ')))
ans = ''
for i in range(nums):
    if test_nums[i] <re:
        ans += str(test_nums[i])+ ' '
ans.strip()
print(ans)
