def solution(today, terms, privacies):
    answer = []
    terms_key = {}
    for term in terms:
        terms_key[term.split(" ")[0]] = int(term.split(" ")[1])
        
    for i in range(len(privacies)):
        created = privacies[i].split(" ")[0]
        term = privacies[i].split(" ")[1]
        
        if verify_expiration(today,created,terms_key[term]):
            answer.append(i+1)
    return answer

def verify_expiration(today, date, month):
    ep_year,ep_month,ep_day = map(int, date.split("."))
    ep_day -= 1
    ep_month += month
    
    if ep_day <= 0:
        ep_day = 28
        ep_month -= 1
    if (ep_month > 12):
        div,mod = divmod((ep_month),12)
        if mod == 0:
            div -= 1
            mod = 12
        ep_year += div
        ep_month = mod
    return True if int(''.join(today.split("."))) > int(str(ep_year)+str(ep_month).zfill(2)+str(ep_day).zfill(2)) else False