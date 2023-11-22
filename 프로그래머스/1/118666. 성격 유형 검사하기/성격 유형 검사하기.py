def solution(survey, choices):
    point = {'R': 0,'T': 0, 'C': 0,'F': 0, 'J': 0,'M': 0, 'A': 0, 'N':0}
    mbti = [('R','T'),('C','F'),('J','M'),('A','N')]
    answer = ''
    for q, p in zip(survey,choices):
        if p >= 5:
            point[q[1]] += p-4
        elif p <= 3:
            point[q[0]] += abs(p-4)
    
    for a,b in mbti:
        if point[a] >= point[b]:
            answer += a
        else:
            answer += b
    return answer
