import sys
num = int(sys.stdin.readline())

for i in range(9):
    sec = i+1
    third = num*(i+1)
    print(str(num)+' * '+str(sec) + ' = '+str(third))