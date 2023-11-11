def solution(cards1, cards2, goal):
    for word in goal:
        if len(cards1) >= 1 and word == cards1[0]:
            cards1.remove(word)
        elif len(cards2) >= 1 and word == cards2[0]:
            cards2.remove(word)
        else:
            return "No"
    return "Yes"