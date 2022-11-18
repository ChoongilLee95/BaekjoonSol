import sys
from collections import defaultdict, deque
from bisect import bisect_left
input = sys.stdin.readline

text_idx = defaultdict(deque)

str_1 = input().strip()
str_2 = input().strip()
str_1_len = len(str_1)
str_2_len = len(str_2)


answer = [str_1_len]

for idx in range(str_1_len):
    text_idx[str_1[idx]].appendleft(idx)

for s in str_2:
    for idx in text_idx[s]:
        if answer[-1]< idx:
            answer.append(idx)
        else:
            answer[bisect_left(answer, idx)] = idx
if answer == [str_1_len]:
    print(0)
else:
    print(len(answer))