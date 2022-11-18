import sys
from collections import defaultdict, deque
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

for idx in range(long_len):
    text_idx[long[idx]].append(idx)
# long의 인덱스를 입력하면 값이 나옴
dp = [0]*(long_len)
# max_idx는 long의 idx
max_idx = 0
max_len = 0
if text_idx[short[0]]:
    long_idx = text_idx[short[0]].popleft()
    max = 0
    for long_idx_before in range(long_idx):
        new = dp[long_idx_before]
        max = new if new>max else max
        continue
    max_len = max_len if max_len>max+1 else max+1
    dp[long_idx] = max+1

for s_idx in range(1,short_len):
    if text_idx[short[s_idx]]:
        long_idx = text_idx[short[s_idx]].popleft()
        max = 0
        for long_idx_before in range(long_idx):
            new = dp[long_idx_before]
            max = new if new>max else max
        max_len = max_len if max_len>max+1 else max+1
        dp[long_idx] = max+1
print(max_len)
print(dp)