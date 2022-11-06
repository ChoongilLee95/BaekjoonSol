import sys

def binary_search(li,left:int, right:int,target):
    if left>right:
        return 0
    mid = (left+right)//2
    if li[mid] ==target:
        return mid
    elif li[mid]<target:
        return binary_search(li,mid+1,right,target)
    else:
        return binary_search(li,left,mid-1,target)

num_num  = int(sys.stdin.readline().strip())
nums = list(map(int, sys.stdin.readline().strip().split()))
nums.sort()

pl = 0
pr = num_num-1
target = abs(nums[0] + nums[num_num-1])
while pl <pr:
    if abs(nums[pr]+nums[pl]) <=target:
        target = abs(nums[pr]+nums[pl])
        ans = [nums[pl],nums[pr]]
    if nums[pl] +nums[pr]>0:
        pr-=1
    elif nums[pl] +nums[pr] <0:
        pl +=1
    else:
        ans = [nums[pl],nums[pr]]
        break
print(ans[0],ans[1])