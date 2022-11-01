import sys
import copy
num  = int(sys.stdin.readline().strip())
candi = list(range(num))

def tlqkf(n:int,k:int,ans:int,candi:list, done:list):
    if k==n-1:
        for i in candi:
            switch_1 = 0
            for j in done:
                if (i-j[0])/(k-j[1])==1 or (i-j[0])/(k-j[1])==-1:
                    switch_1=1
                    break
            if switch_1:
                continue
            else:
                ans +=1
        return ans
    else:
        for i in candi:
            switch_1 = 0
            for j in done:
                if (i-j[0])/(k-j[1])==1 or (i-j[0])/(k-j[1])==-1:
                    switch_1=1
                    break
            if switch_1:
                continue
            else:
                done.append([i,k])
                put_candi=copy.deepcopy(candi)
                put_candi.remove(i)
                ans =tlqkf(n,k+1,ans,put_candi,done)
                candi.sort()
                done.pop()
        return ans


print(tlqkf(num,0,0,candi,[]))

