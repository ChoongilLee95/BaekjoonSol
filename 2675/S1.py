import sys

num_tc  = int(sys.stdin.readline().strip())

for tc in range(num_tc):
    ans = ''
    re_num, str1 = sys.stdin.readline().strip().split(' ')
    for al in str1:
        ans += al*int(re_num)
    print(ans)