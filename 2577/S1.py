import sys

mul = 1
for i in range(3):
    mul *=  int(sys.stdin.readline())

mul = str(mul)
for i in range(0,10):
    num_count = mul.count(str(i))
    print(num_count)
