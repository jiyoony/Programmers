def solution(s):
    answer = 0
    first_letter = ''
    while(len(s) > 1):
        first_letter = s[0]
        diff = 0
        same = 1
        for i in range(1,len(s)):
            if first_letter == s[i]:
                same += 1
            else: 
                diff += 1
            if same == diff:
                answer += 1
                s=s[same+diff:]
                break
            if i == len(s)-1:
                answer += 1
                s=''
                break
    
    answer = answer + 1 if (len(s) == 1) else answer
    return answer
