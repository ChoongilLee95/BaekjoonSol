import sys

num_num  = int(sys.stdin.readline().strip())
num_list =[]
num_dict = dict()
for i in range(num_num):
    num = int(sys.stdin.readline().strip())
    if num in num_dict:
        num_dict[num] +=1
    else:
        num_dict[num] =1
for i in range(1,10001):
    if i in num_dict:
        for j in range(num_dict[i]):
            print(i)

