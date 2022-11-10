import sys

num  = int(sys.stdin.readline().strip())

nums = list(map(int,sys.stdin.readline().strip().split()))

len_list = [1]

maxi = 1
max_num = nums[0]
for i in range(1,num):
    new = 1
    if nums[i] > max_num:
        new = maxi+1
        max_num = nums[i]
    else:
        for j in range(0,i): ## 그 전항까지의 자기 보다 작은 수 중 증가하는 부분집합의 길이가 가장 큰애 +1
            if nums[j]<nums[i]:
                if len_list[j] +1 >new:
                    new = len_list[j]+1
    len_list.append(new) ## 이부분이 메모이제이션
    if new>maxi:
        maxi = new
print(maxi)
