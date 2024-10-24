from collections import deque
def solution(s):
    answer = 0
    q = deque(s)
    while q:
        x_cnt, non_cnt = 1,0
        x = q.popleft()
        while q:
            nxt = q.popleft()
            if x == nxt:
                x_cnt += 1
            else:
                non_cnt += 1

            if x_cnt == non_cnt:
                answer += 1
                break
        if x_cnt != non_cnt:
            answer += 1
            
        
    return answer