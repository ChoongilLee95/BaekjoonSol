import sys
b = sys.stdin.readline()
a = sys.stdin.readline()
low3 = int(a[2]) * int(b)
low4 = int(a[1]) * int(b)
low5 = int(a[0]) *int(b)
low6 = low3 + low4*10 + low5*100
print(low3)
print(low4)
print(low5)
print(low6)