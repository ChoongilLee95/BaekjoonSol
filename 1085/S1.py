import sys
x, y, w, h = map(int, sys.stdin.readline().split(' '))

if x*2 > w:
    short_x = w- x
else:
    short_x = x

if y*2 > h:
    short_y = h-y
else:
    short_y = y

if short_x> short_y:
    ans = short_y
else:
    ans = short_x

print(ans)