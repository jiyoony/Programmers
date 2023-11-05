def solution(name, yearning, photo):
    score = {}
    answer = []
    
    for i in range(len(name)):
        score[name[i]] = yearning[i]
        
    for i in range(len(photo)):
        now_score = 0
        for j in range(len(photo[i])):
            if score.get(photo[i][j]):
                now_score += score[photo[i][j]]
        answer.append(now_score)
    return answer