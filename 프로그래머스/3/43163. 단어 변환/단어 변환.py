# bfs
from collections import deque
def solution(begin, target, words):
    if target not in words:
        return 0
    
    visit = [0] * len(words)
    q = deque([(begin,0)])
    change = 0
    while q:
        now, ch = q.popleft()
        if now == target:
            change = ch
            break
        for i,word in enumerate(words):
            if visit[i] == 0 and can_change(now,word):
                q.append((word,ch +1))
                visit[i] = 1
    return change





# 한 글자만 다른지 체크
def can_change(w1,w2):
    diff = 0
    for i,j in zip(list(w1),list(w2)):
        if i != j:
            diff += 1
    return True if diff == 1 else False
    
    
    