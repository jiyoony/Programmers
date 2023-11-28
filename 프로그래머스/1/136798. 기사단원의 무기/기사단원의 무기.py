def solution(number, limit, power):
    divisor = []
    for i in range(1,number+1):
        div_count = 0
        for j in range(1,int(i**0.5)+1):
            if i%j == 0:
                div_count += 2
        if i ** 0.5 % 1 == 0:
            div_count -= 1
        divisor.append(div_count if div_count <= limit else power)
    return sum(divisor)