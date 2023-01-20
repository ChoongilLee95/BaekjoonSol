import sys
from collections import defaultdict
input = sys.stdin.readline

m_c = [-1,0,0,1]
m_r = [0,-1,1,0]

# 자신이 들어갈 위치를 pos 기준으로 찾는 함수
def like(pos):
    ans_pos = (0,0)
    sat_value = 0
    for i in range(4):
        new_col = m_c[i] + pos[0]
        new_row = m_r[i] + pos[1]
        if new_col<1 or new_col>num_col or new_row<1 or new_row >num_col or seat[new_col][new_row]:
            continue
        sat_priority[new_col][new_row] +=1
        if sat_priority[new_col][new_row] > sat_value:
            sat_value = sat_priority[new_col][new_row]
            ans_pos = (new_col,new_row)
    return sat_value, ans_pos

# 들어갈 자리를 기준으로 만족도 갱신(자신+인접) + 자리 기입
def set_sat(pos, student_id):
    seat[pos[0]][pos[1]] = student_id
    for i in range(4):
        new_col = m_c[i] + pos[0]
        new_row = m_r[i] + pos[1]
        if new_col<1 or new_col>num_col or new_row<1 or new_row >num_col:
            continue
        if seat[new_col][new_row]:
            if student_id in student_to_likes[seat[new_col][new_row]]:
                student_to_sat[seat[new_col][new_row]]+=1

    

# 좋아하는 애가 없을 때
def dislike():
    max_value = -1
    for c in range(1,num_col+1):
        for r in range(1, num_col+1):
            value = 0
            if seat[c][r]:
                continue
            for i in range(4):
                new_col = m_c[i] + c
                new_row = m_r[i] + r
                if new_col<1 or new_col>num_col or new_row<1 or new_row >num_col or seat[new_col][new_row]:
                    continue
                value+=1
            if value > max_value:
                max_value = value
                ans_pos = (c,r)
    return ans_pos

num_col = int(input())
student_to_likes = defaultdict()

seat = [[0]*(num_col+1) for i in range(num_col+1)]

student_to_position = defaultdict(int)
student_to_sat = [0]*(num_col**2+1)

sum_sat = 0

student_info = list(map(int, input().strip().split()))
student_id = student_info[0]
student_to_likes[student_id] = student_info[1:]
if num_col>1:
    student_to_position[student_id] = (2,2)
else:
    student_to_position[student_id] = (1,1)
seat[2][2] = student_id


for _ in range((num_col**2)-1):
    sat_priority = [[0]*(num_col+1) for __ in range(num_col+1)]
    student_info = list(map(int, input().strip().split()))
    student_id = student_info[0]
    student_to_likes[student_id] = student_info[1:]
    max_value = 0
    ans_pos = (0,0)
    for j in range(1,5):
        start_pos = student_to_position[student_info[j]]
        if start_pos == 0:
            continue
        value, pos = like(start_pos)
        if value > max_value:
            max_value = value
            ans_pos = pos
            continue
        if value == max_value:
            if pos[0]<ans_pos[0]:
                ans_pos = pos
                continue
            if pos[0] == ans_pos[0] and pos[1] <ans_pos[1]:
                ans_pos= pos
                continue
            continue
    if max_value:
        student_to_sat[student_id] = max_value
        student_to_position[student_id] = ans_pos
    else:
        ans_pos = dislike()
    set_sat(ans_pos, student_id)

ans = 0
for i in range(1, num_col):
    if student_to_sat[i]:
        ans += 10**(student_to_sat[i]-1) 

print(ans)






