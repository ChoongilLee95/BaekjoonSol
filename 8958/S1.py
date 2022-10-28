import sys
num_tc = int(sys.stdin.readline())



for tc in range(num_tc):
    score = 0
    ans = 0
    case = sys.stdin.readline()
    for i in case:
        if i =='O':
            score +=1
        else:
            score = 0
        ans += score
    print(ans)
