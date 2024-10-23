def solution(today, terms, privacies):
    answer = []
    terms_info = {v[0]:int(v[2:])*28 for v in terms}
    
    today_date = to_date(today)
    
    for i, privacy in enumerate(privacies,start=1):
        day,term = privacy.split(" ")
        date = to_date(day)
        if today_date >= date + terms_info[term]:
            answer.append(i)
        
    return answer

def to_date(days):
    year,month,day = map(int,days.split("."))
    return (year - 2000)*12*28 + month*28 + day