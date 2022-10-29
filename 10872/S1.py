import sys

input_num  = int(sys.stdin.readline().strip())

def pac(n:int):
    if n ==0:
        return 1
    else:
        return pac(n-1)*n

print(pac(input_num))


