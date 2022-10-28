import sys
score = sys.stdin.readline()
if len(score) ==2:
    ans = 'F'
elif len(score)==4 or score[0] =='9':
    ans = 'A'
elif score[0] =='8':
    ans = 'B'
elif score[0] =='7':
    ans = 'C'
elif score[0] =='6':
    ans = 'D'
else:
    ans = 'F'
print(ans)