def solution(ingredient):
    answer = 0
    hambuger_stack = []
    for i in ingredient:
        hambuger_stack.append(i)
        
        if hambuger_stack[-4:] == [1,2,3,1]:
            del hambuger_stack[-4:]
            answer += 1    
    
    return answer
        
    