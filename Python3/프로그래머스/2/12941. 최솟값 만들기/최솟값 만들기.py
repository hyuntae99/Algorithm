def solution(A,B):
    answer = 0
    A.sort()
    B.sort(reverse=True)
    
    n = len(A) 
    b = len(B)
    if n > b:
        n = b
        
    for i in range(n):
        answer += A[i] * B[i]

    return answer