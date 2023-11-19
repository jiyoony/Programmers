def solution(t, p):
    answer = 0
    sub_len = len(p)
    for i in range(len(t)-sub_len+1):
        answer += 1 if int(t[i:i+sub_len]) <= int(p) else 0
    return answer