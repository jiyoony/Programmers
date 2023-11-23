def solution(a, b, n):
    answer = 0
    while(n >= a):
        get, left = divmod(n,a)
        answer += b * get
        n = b*get + left
        
    return answer