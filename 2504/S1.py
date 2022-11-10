import sys


a  = sys.stdin.readline().strip()
opstack = []
outstack = []
for i in range(len(a)):
    if a[i] == '(':
        if a[i+1] == ')':
            outstack.append(2)
        else:
            opstack.append('(')
    elif a[i] == ')':
        if a[i-1] == '(':
            pass
        else:
            while opstack[-1] !='(':
                outstack.append(opstack.pop())
            opstack.pop()
            if len(opstack):
                while opstack[-1] =='*':
                    outstack.append(opstack.pop())
            opstack.append('*')
            outstack.append(2)