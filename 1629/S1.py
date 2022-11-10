import sys
sys.setrecursionlimit(10**6)
num,jisu,num2  = map(int, sys.stdin.readline().strip().split())

def gogo(n,j,n2):
    if j ==2:
        return ((n%n2)**2)%n2
    elif j ==3:
        return ((n%n2)**3)%n2
    new = j//2
    if j%2==0:
        return (gogo(n,new,n2)**2)%n2
    else:
        return ((gogo(n,new,n2)**2)*n)%n2
print(gogo(num,jisu,num2))