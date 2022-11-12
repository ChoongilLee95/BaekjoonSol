import sys
from collections import defaultdict
import heapq
## 중간에 다되면 멈추려면?

def combine_union(a1,a2):
    if union_node[a1] < union_node[a2]:
        big = union_node[a2]
        small = union_node[a1]
    else:
        big = union_node[a1]
        small = union_node[a2]
    for i in union_component[big]:
        union_node[i] = small
        union_component[small].append(i)
    union_component[big] = []


def check_union(a1,a2):
    if union_node[a1] == union_node[a2]:
        return True
    else:
        return False
union_component = defaultdict(list)
union_node = dict()
dict_line = defaultdict(list)
lines_heap = []

num_node,num_line = map(int, sys.stdin.readline().strip().split())

for _ in range(num_line):
    a1,a2,cr  = map(int, sys.stdin.readline().strip().split())
    dict_line[cr].append([a1,a2])
    union_node[a1] = a1
    if not union_component[a1]:
        union_component[a1].append(a1)
    if union_component[a2]==[]:
        union_component[a2].append(a2)
    union_node[a2] = a2
    heapq.heappush(lines_heap,cr)
answer = 0
for _ in range(num_line):
    if len(union_component[1]) == num_node:
        break
    cr = heapq.heappop(lines_heap)
    nodes = dict_line[cr].pop()
    if not check_union(nodes[0],nodes[1]):
        combine_union(nodes[0],nodes[1])
        answer +=cr
print(answer)


