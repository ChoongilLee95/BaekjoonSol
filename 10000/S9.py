import sys
n  = int(sys.stdin.readline().strip())
num_list = []
for _ in range(n):
    a,b = map(int,sys.stdin.readline().strip().split())
    x1, x2 = a-b,a+b
    num_list.append([x1,x2,x1])
num_list.sort(key=lambda x: (x[0], -x[1]))
ans = 1+n
deque_list = []
for i in range(n):
    new = num_list[i]
    if deque_list:
        while deque_list[-1][2] < new[0]:
            deque_list.pop()
            if not deque_list:
                break
        if deque_list:
            if deque_list[-1][2] == new[0]:
                deque_list[-1][2] = new[1]
                if deque_list[-1][2] == deque_list[-1][1]:
                    deque_list.pop()
                    ans +=1
    deque_list.append(new)
print(ans)