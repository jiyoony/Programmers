from collections import Counter
def solution(k, tangerine):
    answer = 0
    tan_dict = sorted(dict(Counter(tangerine)).items(), key=lambda x: x[1], reverse=True)
    cur_count = 0
    for i, count in tan_dict:
        cur_count += count
        answer += 1
        if cur_count >= k:
            break
    
    return answer