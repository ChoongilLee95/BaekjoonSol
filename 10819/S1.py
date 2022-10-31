import sys

num_num  = int(sys.stdin.readline().strip())

num_list = list(map(int, sys.stdin.readline().strip().split()))

num_list.sort()
sum_nums = 0
if num_num%2:
    for i in range(num_num//2-1):
        sum_nums += (-num_list[i]+num_list[num_num-i-1])*2
    if num_list[num_num//2+1] - num_list[num_num//2] > num_list[num_num//2] - num_list[num_num//2-1]:
        sum_nums += -num_list[num_num//2]- num_list[num_num//2-1]+num_list[num_num//2+1]*2
    else:
        sum_nums += +num_list[num_num//2]- num_list[num_num//2-1]*2+num_list[num_num//2+1]
else:
    for i in range(num_num//2-1):
        sum_nums += (-num_list[i]+num_list[num_num-i-1])*2
    sum_nums -= num_list[num_num//2-1] -num_list[num_num//2]

print(sum_nums)

