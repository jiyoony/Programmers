def solution(babbling):
    answer = 0
    canSay = ["aya", "ye", "woo", "ma"]
    beforeSaid = ""
    for word in babbling:
        say = ""
        beforeSaid = ""
        for i in range(len(word)):
            say += word[i]
            if (say in canSay) and beforeSaid != say:
                beforeSaid = say
                say = ""
            if i+1 == len(word) and say == "":
                answer += 1
                
    return answer