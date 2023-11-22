import re 
def solution(s, skip, index):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    newAlphabet = re.sub('['+skip+']','',alphabet)
    answer = ''
    for i in s:
        next_index = newAlphabet.find(i)+index
        if next_index >= len(newAlphabet):
            next_index = next_index % len(newAlphabet) - len(newAlphabet)
        answer += newAlphabet[next_index]
    return answer