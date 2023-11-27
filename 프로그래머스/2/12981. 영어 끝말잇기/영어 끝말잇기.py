def solution(n, words):
    for i, word in enumerate(words):
        turn = i+1
        if i == 0:
            continue
        if (words[:i+1].count(word) > 1):
            return [turn%n if (turn%n != 0) else n, (turn+n-1)//n]
        if words[i-1][-1] != word[0]:
            return [turn%n if (turn%n != 0) else n, (turn+n-1)//n]

    return [0,0]