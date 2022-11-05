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
nums.append(0)
nums.sort()
breaker = 0
if nums[0] ==0:
    print(nums[1],nums[2])
elif nums[-1]==0:
    nums.pop()
    x = nums.pop()
    y = nums.pop()
    print(y,x)
else:
    k = 0
    a = binary_search(nums,0,num_num,0)
    ans_list = []
    if a >1:
        ans_list.append([nums[a-2],nums[a-1]])
    if num_num-a>1:
        ans_list.append([nums[a+1],nums[a+2]])
    if num_num-a>0 and a>0:
        ans_list.append([nums[a-1],nums[a+1]])
    ans = ans_list.pop()
    for i in ans_list:
        if abs(i[0]+i[1]) < abs(ans[0]+ans[1]):
            ans = i
    target = abs(ans[0]+ans[1])
    while nums[k]<0:
        for j in range(target):
            if binary_search(nums,a+1,num_num,-(nums[k]-j)):
                ans = [nums[k],-(nums[k]-j)]
                if j !=0:
                    target=j
                    break
                else:
                    breaker = 1
                    break
            if j:
                if binary_search(nums,a+1,num_num,-(nums[k]+j)):
                    ans = [nums[k],-(nums[k]+j)]
                    if j !=0:
                        target=j
                        break
                    else:
                        breaker = 1
                        break
        if breaker==1:
            break
        k+=1

    print(ans[0],ans[1])
