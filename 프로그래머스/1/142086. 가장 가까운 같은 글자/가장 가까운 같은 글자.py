def solution(s):
    answer = []
    for i in range(len(s)):
        s_reverse = s[0:i][::-1]
        answer.append((s_reverse.find(s[i])+1 if s[i] in s_reverse else -1))
        
    return answer