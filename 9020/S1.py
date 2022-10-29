import sys

num_tc  = int(sys.stdin.readline().strip())

def sosu(n:int):
    root_n = int(n**(1/2))
    if n ==2:
        ans = True
    elif root_n == n**(1/2):
        ans =False
    elif root_n>2:
        ans = True
        for i in range(3,root_n+1,2):
            if n%i==0:
                ans = False
                break
            else:
                continue
    else:
        ans=True
    return ans


for tc in range(num_tc):
    upper_list = []
    lower_list = []
    ans =''
    n = int(sys.stdin.readline().strip())
    lower_list.append(2)
    for i in range(3,n+1,2):
        if sosu(i):
            if i ==n/2:
                ans = f'{i} {i}'
                break
            elif i>n/2:
                upper_list.append(i)
            else:
                lower_list.append(i)
    if ans =='':
        for k in upper_list:
            for j in lower_list:
                if k+j>n:
                    break
                elif k+j ==n:
                    ans = f'{j} {k}'
                    break
                else:
                    continue
            if ans!='':
                break
    print(ans)




