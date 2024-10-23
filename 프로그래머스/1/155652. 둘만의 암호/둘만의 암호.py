def solution(s, skip, index):
    answer = ''
    alphabet = list('abcdefghijklmnopqrstuvwxyz')
    skip_list = list(skip)
    target_alphabet = [x for x in alphabet if x not in skip_list]
    for a in s:
        answer += target_alphabet[(target_alphabet.index(a)+index)%len(target_alphabet)]
    return answer