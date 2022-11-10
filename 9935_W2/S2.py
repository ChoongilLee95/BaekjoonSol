import sys

string  = sys.stdin.readline().strip()

bomb = sys.stdin.readline().strip()

answer = []

def boom():
    if ''.join(answer[len(answer)-len(bomb):]) == bomb:
        return True
    else:
        return False
for i in string:
    answer.append(i)
    if i == bomb[-1]:
        if boom():
            for _ in bomb:
                answer.pop()
if answer:
    print(''.join(answer))
else:
    print('FRULA')