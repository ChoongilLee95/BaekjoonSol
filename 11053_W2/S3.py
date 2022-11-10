## lowerbound를 이용
# 최장 수열의 정보를 저장하는 L에 수열의 새로운 요소를 넣는다.
# 마지막 요소보다 크다면 그냥 추가
# 아니라면 그 수의 lowerbound를 찾아 바꾼다.(이분탐색)



import sys

num  = int(sys.stdin.readline().strip())

nums = list(map(int,sys.stdin.readline().strip().split()))

L = [nums[0]]

for i in range(1,num):
    if nums[i]>L[-1]:
        L.append(nums[i])
    else:
        left = 0
        right = len(L)-1
        while left <= right:
            mid = (left+right)//2
            if L[mid] ==nums[i]:
                break
            elif L[mid]<nums[i]:
                left = mid+1
            else:
                old_mid = mid
                right = mid-1
        else:
            L[old_mid] = nums[i]
print(len(L))

