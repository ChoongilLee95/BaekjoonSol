import sys

n  = int(sys.stdin.readline().strip())

for i in range(n):
    tc = sys.stdin.readline().strip()
    stack = []
    breaker=0
    for ch in tc:
        if ch =='(':
            stack.append(1)
        else:
            if len(stack):
                stack.pop()
            else:
                breaker =1
                break
    if len(stack):
        print('NO')
    else:
        if breaker:
            print('NO')
        else:
            print('YES')

