# 투포인터
def solution(n):
    answer = 1
    start, end, sum = 1, 1, 1
    while end < n:
        if sum < n:
            end += 1
            sum += end
        else:
            if n == sum: answer += 1
            sum -= start
            start += 1
        
    return answer