import sys
import copy
num  = int(sys.stdin.readline().strip())

candi = [[j for j in range(num)] for i in range(num)]
def tlqkf_start(n,k):
    if n == 1:
        return 1
    ans = 0
    def tlqkf(n:int,k:int,candi:list):
        nonlocal ans
        if k==n-1:
            ans +=len(candi[k])
            return ans
        else:
            for x_axis in candi[k]:
                new_candi = copy.deepcopy(candi)
                for y_axis in range(k+1,n):
                    if y_axis+x_axis-k in new_candi[y_axis]:
                        new_candi[y_axis].remove(y_axis+x_axis-k)
                    if -y_axis+x_axis+k in new_candi[y_axis]:
                        new_candi[y_axis].remove(-y_axis+x_axis+k)
                    if x_axis in new_candi[y_axis]:
                        new_candi[y_axis].remove(x_axis)
                tlqkf(n,k+1,new_candi)
    for i in range(n//2):
        new_candi = copy.deepcopy(candi)
        for y_axis in range(k+1,n):
            if y_axis+i-k in new_candi[y_axis]:
                new_candi[y_axis].remove(y_axis+i-k)
            if -y_axis+i+k in new_candi[y_axis]:
                new_candi[y_axis].remove(-y_axis+i+k)
            if i in new_candi[y_axis]:
                new_candi[y_axis].remove(i)
        tlqkf(n,k+1,new_candi)
    ans*=2
    if n%2==0:
        return ans
    else:
        i = n//2
        for y_axis in range(k+1,n):
            if y_axis+i-k in new_candi[y_axis]:
                new_candi[y_axis].remove(y_axis+i-k)
            if -y_axis+i+k in new_candi[y_axis]:
                new_candi[y_axis].remove(-y_axis+i+k)
            if i in new_candi[y_axis]:
                new_candi[y_axis].remove(i)
        tlqkf(n,k+1,new_candi)
        return ans
print(tlqkf_start(num,0))
