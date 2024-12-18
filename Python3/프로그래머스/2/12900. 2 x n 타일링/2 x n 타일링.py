def solution(n):
    d = [0] * (n+2)
    d[1] = 1
    d[2] = 1
    
    for i in range(3, n+2):
        d[i] = (d[i-1] + d[i-2]) % 1000000007
    
    return d[n+1]