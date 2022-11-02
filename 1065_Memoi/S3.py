import sys

a  = int(sys.stdin.readline().strip())


def hansu(n : int):
    k = 10**(len(str(n))-1)
    l = int(str(n)[0])-int(str(n)[1])
    t = n-(n%k)
    cha = n-t -n//10
    if cha ==0:
        if l ==0:
            return True
        else:
            return False
    if l<0:
        if cha <0:
            return False
        else:
            l = -l
            m = f'{l}'*(len(str(n))-1)
            if cha%int(m)==0:
                return True
            else:
                return False
    elif l>0:
        if cha >0:
            return False
        else:
            m = f'{l}'*(len(str(n))-1)
            if cha%int(m)==0:
                return True
            else:
                return False


def all_hansu(n: int):
    ans = []
    if n ==1:
        return list(range(1,10))
    elif n==2:
        return list(range(10,100))
    else:
        for i in all_hansu(n-1):
            str_i=str(i)
            cha = int(str_i[1])-int(str_i[0])
            if 0<=cha+int(str_i[n-2])<=9:
                str_i+= str(cha+int(str_i[n-2]))
                ans.append(int(str_i))
        return(ans)

def find_all_hansu(n:int):
    str_n = str(n)
    ans =0
    if n>99:
        for i in range(1,len(str_n)):
            ans+=len(all_hansu(i))
        for i in range(10**(len(str_n)-1),n+1):
            if hansu(i):
                ans+=1
    else:
        ans = n
    return ans

print(find_all_hansu(a))


