import math
def lcm(a,b):
    return int(a * b / math.gcd(a,b))

def solution(arr):
    answer = arr[0]
    for i in arr[1:]:
        answer = lcm(answer,i)
    return answer

    