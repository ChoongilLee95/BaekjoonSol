import sys
from collections import defaultdict
sys.setrecursionlimit(10**6)
def postorder(s):
    if tree_dict[s] !=[]:
        for i in tree_dict[s]:
            postorder(i)
    print(s)


tree = []
tree_dict = defaultdict(list)
while True:
    num  = sys.stdin.readline().strip()
    if num =='':
        break
    num = int(num)
    if tree:
        if tree[-1]>num: ### 왼쪽
            tree_dict[tree[-1]].append(num)
            tree.append(num)
        else: ## 오른쪽
            while tree[-1]<num:
                node = tree.pop()
                if tree ==[]:
                    break
            tree_dict[node].append(num)
            tree.append(num)
    else:
        start = num
        tree.append(num)

postorder(start)

