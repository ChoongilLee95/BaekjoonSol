import sys

target  = int(sys.stdin.readline().strip())

def hansu(n:int):
    ans = 99
    num = n
    ## 기존memo를 이용하여 n보다 자리 수가 적은 한수들을 memo한다
    def hansu_before(n: int):
        ans_list = []
        nonlocal ans
        for i in memo[n-3]:
            str_i = str(i)
            cha = int(str_i[1])-int(str_i[0])
            if 0<=cha+int(str_i[n-2])<=9:
                str_i+= str(cha+int(str_i[n-2]))
                ans_list.append(int(str_i))
                ans+=1
        memo.append(ans_list)
    # 기존 memo를 이용하여 n이랑 같은 자리 수 이면서 n보다 작은 한수의 수를 추가한다
    def hansu_now(n: int):
        nonlocal ans
        nonlocal num
        for i in memo[n-3]:
            str_i = str(i)
            cha = int(str_i[1])-int(str_i[0])
            if 0<=cha+int(str_i[n-2])<=9 and num>=int(str_i+ str(cha+int(str_i[n-2]))):
                ans+=1
    len_n = len(str(n))
    if len_n < 3:
        return n
    memo = []
    memo.append(list(range(10,100)))
    for i in range(3,len_n):
        hansu_before(i)
    hansu_now(len_n)
    return ans
print(hansu(target))
