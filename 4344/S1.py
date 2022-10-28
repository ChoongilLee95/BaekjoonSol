import sys

num_tc = int(sys.stdin.readline())

for tc in range(num_tc):
    aver = 0
    aver_p = 0
    scores = list(map(int, sys.stdin.readline().split()))
    num_people = scores.pop(0)
    aver = sum(scores)//num_people
    for i in scores:
        if i > aver:
            aver_p +=1
    ans = round(100*aver_p/num_people,5)
    print(f'{ans:.3f}%')

