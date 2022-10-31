import sys

num_num  = int(sys.stdin.readline().strip())
list_in = []
for i in range(num_num):
    a = int(sys.stdin.readline().strip())
    list_in.append(a)
list_in.sort()
for i in list_in:
    print(i)

