import sys

num  = int(sys.stdin.readline().strip())

def facto(n,k):
    ans = 1
    for i in range(k,n+1):
        ans*=i
    return ans

def combi(n,r):
    return facto(n,r+1) // facto(n - r,1)
for i in range(num):
    num = int(sys.stdin.readline().strip())
    ans = 0
    n3_pos = num//3
    for n3 in range(n3_pos+1):
        n2_pos = (num-n3*3)//2
        for n2 in range(n2_pos+1):
            n1 = num-n3*3-n2*2
            n = n1 + n2+n3
            ans += combi(n,n3)*combi(n-n3,n2)
    print(ans)

