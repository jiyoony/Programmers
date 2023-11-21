def solution(X, Y):
    find_word = ''.join(set(Y)) if (len(X) > len(Y)) else ''.join(set(X))
    answer = []
    for i in find_word:
        if min(X.count(i),Y.count(i)):
            answer.extend([i]*min(X.count(i),Y.count(i)))
    
    
    answer.sort(reverse=True)
    if len(answer) == 0:
        return '-1'
    elif answer.count('0') == len(answer):
        return '0'
    else:
        return ''.join(answer)