def solution(k, score):
    result = []
    top_k = []
    for i in score:
        top_k.append(i)
        top_k = sorted(top_k, reverse=True)[:k]
        result.append(top_k[-1])
    return result