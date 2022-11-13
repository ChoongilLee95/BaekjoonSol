import sys
n  = int(sys.stdin.readline().strip())
num_list = []
for _ in range(n):
    ans = 1
    a,b = map(int,sys.stdin.readline().strip().split())
    x1, x2 = a-b,a+b
    num_list.append([x1,x2,x1])
num_list.sort(key=lambda x: (x[0], x[1]))
ans = 1
deque_list = []
for new in num_list:
    ans +=1
    if deque_list:
        while deque_list[-1][1] <= new[0]:
            poped = deque_list.pop()
            if poped[2]>=poped[1]:
                ans+=1
            if not deque_list:
                break
        for pre in deque_list:
            if pre[1] > new[0]:
                # pre가 new를 포함할때 (뒤쪽 끝이 겹치는거 포함)
                if pre[1]>=new[1]:
                    if new[0] <= pre[2]< new[1]:
                        pre[2] = new[1]
                # new가 pre를 포함할때 (앞쪽이 겹치는거 포함)
                elif new[0] == pre[0]:
                    if new[1] != pre[1]:
                        new[2] = pre[1]
                # new와 pre가 크로스
                else:
                    ans +=1
                    # new가 pre에게 영향
                    if new[0]<= pre[2] < new[1]:
                        pre[2] = new[1]
                    # pre가 new에게 영향
                    if new[2] < pre[1]:
                        new[2] = pre[1]
            else:
                continue
        deque_list.append(new)
    else:
        deque_list.append(new)
while deque_list:
    left = deque_list.pop()
    if left[2] >= left[1]:
        ans +=1
print(ans)