def solution(food):
    answer = ''
    for i,number in enumerate(food):
        count = divmod(number,2)
        answer += str(i)*count[0]
    return answer+'0'+answer[::-1]