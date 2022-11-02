import sys
import copy
num  = int(sys.stdin.readline().strip())
candi = list(range(num))

def tlqkf_start(n,k,candi):
    if n == 1:
        return 1
    ans = 0
    done =[]
    def tlqkf(n:int,k:int,candi):
        nonlocal ans
        if k==n-1:
            if len(candi)==1:
                i = candi[0]
                switch_1 = 1
                for j in done:
                    if (i-j[0])/(k-j[1])==1 or (i-j[0])/(k-j[1])==-1:
                        switch_1=0
                        break
                if switch_1:
                    ans+=1
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
                    new_candi = copy.deepcopy(candi)
                    done.append([i,k])
                    new_candi.remove(i)
                    tlqkf(n,k+1,new_candi)
                    done.pop()
    for i in range(n//2):
        new_candi = copy.deepcopy(candi)
        done.append([i,k])
        new_candi.remove(i)
        tlqkf(n,k+1,new_candi)
        done.pop()
    ans*=2
    if n%2==0:
        return ans
    else:
        done.append([n//2,k])
        candi.remove(n//2)
        tlqkf(n,k+1,candi)
        return ans
print(tlqkf_start(num,0,candi))

