import sys

string  = sys.stdin.readline().strip()
bomb = sys.stdin.readline().strip()
new_string = string
len_b = len(bomb)
len_s = len(string)
stack = []

for idx in range(len_s):
    chra = string[idx]
    if chra == bomb[0]:
        stack.append([chra,idx])
    elif chra == bomb[-1]:
        if len(stack):
            if stack[-1][0]==bomb[len_b-2]:
                a = len_b-1
                while a>1:
                    stack.pop()
                    a-=1
                t = stack.pop()[1]
                new_string = new_string.replace(bomb,'')
    else:
        if len(stack):
            for j in range(1,len(bomb)-1):
                if bomb[j] == chra:
                    if bomb[j-1] == stack[-1][0]:
                        stack.append([chra,idx])

print(new_string)