def solution(data, col, row_begin, row_end):
    data.sort(key=lambda x:(x[col-1], -x[0]))

    ans = []
    for i in range(row_begin, row_end+1):
        idx = i-1
        s = 0
        for d in data[idx]:
            s += (d % i)
        ans.append(s)
        
    res = 0
    for a in ans:
        res ^= a # XOR연산
    
    return res