def solution(s):
    zero,change = 0,0
    while(s != "1"):
        zero += s.count("0")
        s = s.replace("0","")
        s = format(len(s),'b')
        change += 1
    return [change,zero]