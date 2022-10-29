import sys

a  = int(sys.stdin.readline().strip())

def hanoi(n:int):
    if n ==1:
        return 1
    else:
        return hanoi(n-1)*2+1

def hanoi_print(n:int,start:int, end:int):
    other = 6 - start -end
    if n == 1:
        return f'{start} {end}\n'
    else:
        return hanoi_print(n-1, start, other)+f'{start} {end}\n' +hanoi_print(n-1, other,end)

print(hanoi(a))
if a <21:
    print(hanoi_print(a,1,3))
