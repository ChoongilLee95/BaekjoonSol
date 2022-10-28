import sys


ans_num = 0
ans_index = 0

for i in range(9):
    num = int(sys.stdin.readline())
    if num >ans_num:
        ans_num = num
        ans_index = i
print(ans_num)
print(ans_index+1)