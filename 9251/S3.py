import sys
from collections import defaultdict, deque
from bisect import bisect_left
input = sys.stdin.readline

text_idx = defaultdict(deque)

str_1 = input().strip()
str_2 = input().strip()
str_1_len = len(str_1)
str_2_len = len(str_2)
if str_1_len > str_2_len:
    long = str_1
    short = str_2
    long_len = str_1_len
    short_len = str_2_len
else:
    long = str_2
    short = str_1
    long_len = str_2_len
    short_len = str_1_len

answer = [long_len]

for idx in range(long_len):
    text_idx[long[idx]].appendleft(idx)

for s in short:
    for idx in text_idx[s]:
        if answer[-1]< idx:
            answer.append(idx)
        else:
            answer[bisect_left(answer, idx)] = idx
if answer == [long_len]:
    print(0)
else:
    print(len(answer))