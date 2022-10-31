import sys

total_sum_height = 0
height_list = []
for i in range(9):
    num  = int(sys.stdin.readline().strip())
    height_list.append(num)
    total_sum_height += num
alf =0
target = total_sum_height - 100
for i in range(9):
    for j in range(i+1,9):
        if height_list[i]+height_list[j] ==target:
            height_list.pop(i)
            height_list.pop(j-1)
            alf = 1
            break
    if alf:
        break

height_list.sort()
for i in height_list:
    print(i)



