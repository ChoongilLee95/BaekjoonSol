import sys

target  = int(sys.stdin.readline().strip())

def hansu(n:int):
    first = list(range(1,10))
    str_n = str(n)
    ans = 0
    if len(str_n)==1:
        return n
    elif len(str_n)==2:
        return n
    else:
        max_turm = 8//(len(str_n)-1)
        for i in first:
            if i >int(str_n[0]):
                break
            else:
                for j in range(max_turm+1):
                    str_ans = f'{i}'
                    over = 0
                    for k in range(len(str_n)):
                        if i ==int(str_n[0]):
                            print('스텝1')
                            if int(str_ans[k-1])+j>int(str_n[k]):
                                print('스텝2')
                                over=1
                                print(f'over :{over}')
                                break
                            else:
                                print(int(str_ans[k-1]))
                                print(int(str_n[k]))
                                str_ans += str(int(str_ans[k])+j)
                                print('스텝2-2')

                        elif i <int(str_n[0]):
                            if int(str_ans[k-1])+j>9:
                                over=1
                                break
                            else:
                                str_ans += str(int(str_ans[k])+j)
                        if over==1:
                            print('스텝3-1')
                            break
                        else:
                            print('스텝3-2')
                            continue
                    if len(str_ans)==len(str_n):
                        ans+=1
                        print('스텝3')
        for i in range(1,len(str_n)):
            ans+=len(all_hansu(i))
        return ans


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


print(hansu(target))