import sys
import copy
num  = int(sys.stdin.readline().strip())

candi = [[j for j in range(num)] for i in range(num)]

def tlqkf(n:int,k:int,ans:int,candi:list):
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
            ans =tlqkf(n,k+1,ans,new_candi)
    return ans
print(tlqkf(num,0,0,candi))

### set 써서 다시하기
