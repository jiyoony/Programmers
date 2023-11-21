import re
def solution(dartResult):
    dart = re.findall("([0-9]+)([SDT]+)([*#]?)",dartResult)
    answer = [0] * len(dart)
    for i, (p,b,s) in enumerate(dart):
        answer[i] += int(p)
        
        if b == "D":
            answer[i] = answer[i] ** 2
        elif b == "T":
            answer[i] = answer[i] ** 3
        
        if s == "*":
            answer[i] *= 2
            if i != 0:
                answer[i-1] *= 2
        elif s == "#":
            answer[i] *= -1
        
            
    return sum(answer)