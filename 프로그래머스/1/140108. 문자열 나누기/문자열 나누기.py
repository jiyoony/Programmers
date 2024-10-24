def solution(s):
    answer = 0
    while s:
        x = s[0]
        x_cnt, non_cnt = 0, 0
        for j in range(len(s)):
            if s[j] == x:
                x_cnt += 1
            else:
                non_cnt += 1
            if x_cnt == non_cnt:
                answer += 1
                s = s[j+1:]
                break
        if x_cnt != non_cnt:
            answer += 1
            break
        
    return answer