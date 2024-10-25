def solution(number, limit, power):
    answer = 0
    for i in range(1,number+1):
        divisors = divisor(i)
        if divisors > limit:
            answer += power
        else: 
            answer += divisors
    return answer

def divisor(num):
    divisors = []
    for i in range(1,int(num**0.5)+1):
        if num % i == 0:
            divisors.extend([i,num//i])
    return len(set(divisors))
    