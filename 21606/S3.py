import sys

num_vtx  = int(sys.stdin.readline().strip())

inOut = '0'+sys.stdin.readline().strip()
Vroot = [i for i in range(num_vtx+1)]

Vroot_con = [[] for _ in range(num_vtx+1)]

def find(n):
    if n != Vroot[n]:
        Vroot[n] = find(Vroot[n])
    return Vroot[n]
ans = 0
for _ in range(num_vtx-1):
    a1, a2 = map(int,sys.stdin.readline().strip().split())
    if inOut[a1] =='1' and inOut[a2] == '1':
        ans +=2
    elif inOut[a1] == '1' and inOut[a2]=='0':
        Vroot_con[Vroot[a2]].append(a1)
    elif inOut[a1] == '0' and inOut[a2]=='1':
        Vroot_con[Vroot[a1]].append(a2)
    else:
        root1 = Vroot[a1]
        root2 = Vroot[a2]
        if root1 > root2:
            Vroot[root1] = root2
            Vroot_con[root2] += Vroot_con[root1]
            Vroot_con[root1] = []
        else:
            Vroot[root2] = root1
            Vroot_con[root1] += Vroot_con[root2]
            Vroot_con[root2] = []
for i in Vroot_con:
    if i:
        ans +=len(i)*(len(i)-1)


print(ans)