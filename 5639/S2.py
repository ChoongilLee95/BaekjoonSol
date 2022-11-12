import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

a = []
while True:
    try: n = int(input())
    except: break
    a.append(n)

def post_order(st, en):
    if st > en: return
    temp = 0
    init_v = a[st]
    for i in range(st+1, en+1):
        if init_v < a[i]:
            temp = i
            break
    else: temp = en + 1
    post_order(st+1, temp - 1)
    post_order(temp, en)
    print(init_v)

post_order(0, len(a)-1)