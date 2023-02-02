import sys

input = sys.stdin.readline

num_slot = int(input())

honey_list = list(map(int, input().strip().split()))


def honey_bee(num_slot):
    total_honey = 0
    len_honey = num_slot
    max_honey = 0
    for i in range(len_honey):
        total_honey += honey_list[i]
        if 0<i<len_honey-1 and honey_list[i] > max_honey:
            max_honey = honey_list[i]

    # case 0 꿀통을 중간
    sum_honey_m = total_honey - honey_list[0] - honey_list[-1] + max_honey

    # case 1 벌a가 왼쪽 끝 꿀통 오른쪽 끝
    # print(honey_list)
    # print(total_honey)
    sum_honey_l = (total_honey-honey_list[0])*2
    # print(sum_honey_l)
    for i in range(1,len_honey-1):
        if i == len_honey-2:
            sum_honey_l-= honey_list[i]*2
            break
        if honey_list[i+1]*2 < honey_list[i]:
            # print(sum_honey_l, i)
            sum_honey_l-=honey_list[i]
        else:
            # print(sum_honey_l, i)
            sum_honey_l-=honey_list[i]*2
            break
    # print(f'i = {i}')

    # case 2 
    sum_honey_r = (total_honey-honey_list[-1])*2
    for i in range(len_honey-2, 0, -1):
        if i == 1:
            sum_honey_r-= honey_list[i]*2
            break
        if honey_list[i-1]*2 < honey_list[i]:
            sum_honey_r -= honey_list[i]
        else:
            sum_honey_r -= honey_list[i]*2
            break
    # print(f'i = {i}')
    # print(sum_honey_l, sum_honey_m, sum_honey_r)
    if sum_honey_l < sum_honey_r:
        sum_honey_l =sum_honey_r
    if sum_honey_l < sum_honey_m:
        sum_honey_l = sum_honey_m
    return sum_honey_l

print(honey_bee(num_slot))