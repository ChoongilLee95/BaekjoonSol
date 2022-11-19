import sys
import heapq

input = sys.stdin.readline

num_m = int(input())

list_n = []

for _ in range(num_m-1):
    a,b =map(int, input().split())
    list_n.append(a)
a,b = map(int,input().split())
list_n.append(a)
list_n.append(b)

left = list_n[0]
right = list_n[-1]
# 비트 마스킹, n개의 0을 표현하기 위해선 0001 2**(idx)
# 해당 인덱스의 1인지 0인지 확인 방법
# 2**(i-1)
# 0~num_m-2 num_m-1개의 0
for_now = 2**(num_m-1)

# now리스트에서 하나 빼는 때에 더해지느 수를 리턴하는 함수
def popping(idx,arr):
    global num_m
    n_l = idx-1
    n_r = idx+1
    while -1<n_l and arr[n_l] == 1:
        n_l-=1
    if n_l == -1:
        n_l = left
    else:
        n_l = list_n[n_l+1]
    while n_r<num_m-1 and arr[n_r] == 1:
        n_r +=1
    if n_r==num_m-1:
        n_r = right
    else:
        n_r = list_n[n_r+1]
    return n_l*n_r*list_n[idx+1]
# 튜플이 들어갈 예정 대응되는 값은 빠지면서 더해진 애들의 합
dp = dict()

# 작업큐가 들어가는 곳 [빼진수의 합,(튜플)]
# 작업의 타당성을 큐에 들어갈떄 한번 나올때 한번 체크한다.
que = []

for i in range(0,num_m-1):
    for_now[i] = 1
    a = popping(i,for_now)
    b = tuple(for_now)
    heapq.heappush(que,(a,b))
    dp[b] = a
    for_now[i] = 0
m_s = sys.maxsize
while que:
    total, tu = heapq.heappop(que)
    if dp[tu]<total:
        continue
    li = list(tu)
    for i in range(0,num_m-1):
        if tu[i] == 1:
            continue
        li[i] = 1
        b =tuple(li)
        a = popping(i,b)
        if dp.get(b,m_s) > total+a:
            dp[b] = total+a
            heapq.heappush(que,(a+total,b))
        li[i] = 0
ans = tuple([1]*(num_m-1))
print(dp[ans])

print(2**500)



