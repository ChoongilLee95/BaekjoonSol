import sys

def preorder(s):
    global answer
    left,right = tree[s][0],tree[s][1]
    answer+=s
    if left != '.':
        preorder(left)
    if right != '.':
        preorder(right)
def inorder(s):
    global answer
    left,right = tree[s][0],tree[s][1]
    if left != '.':
        inorder(left)
    answer +=s
    if right != '.':
        inorder(right)
def postorder(s):
    global answer
    left,right = tree[s][0],tree[s][1]
    if left != '.':
        postorder(left)
    if right != '.':
        postorder(right)
    answer +=s



tree = {}
answer = ''
n  = int(sys.stdin.readline().strip())
for _ in range(n):
    root,left,right = map(str,sys.stdin.readline().strip().split())
    tree[root] = [left, right]
    if _ == 0:
        start = root
preorder(start)
print(answer)
answer = ''
inorder(start)
print(answer)
answer=''
postorder(start)
print(answer)
