def solution(s):
    before = dict()
    answer = []
    
    for i,k in enumerate(list(s)):
        if k in before.keys():
            answer.append(i-before[k])
        else:
            answer.append(-1)
        before[k] = i
    
    return answer