from collections import deque
def solution(s):
    deq = deque(s)
    close = 0
    while(deq):
        next = deq.pop()
        if (next == '('):
            close -= 1
        else: close += 1
        if close < 0: return False
    return True if (close == 0) else False