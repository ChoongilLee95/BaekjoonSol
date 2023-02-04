import sys
input = sys.stdin.readline

N, M = list(map(int, input().strip().split()))

kwords = set()
used = set()
for _ in range(N):
    kwords.add(input().strip())

for _ in range(M):
    used = list(input().strip().split(','))
    for i in used:
        if i in kwords:
            kwords.remove(i)
    print(len(kwords))


