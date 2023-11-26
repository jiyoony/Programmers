def solution(data, ext, val_ext, sort_by):
    answer = []
    sort = ["code","date","maximum","remain"]
    
    idx = sort.index(ext)
    sort_idx = sort.index(sort_by)
    for i in data:
        if i[idx] < val_ext:
            answer.append(i)
    
    answer.sort(key = lambda answer:answer[sort_idx])
    return answer