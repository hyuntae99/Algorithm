def solution(A, B):
    A.sort()  # A를 오름차순 정렬
    B.sort()  # B를 오름차순 정렬
    
    a = 0  # A의 포인터
    b = 0  # B의 포인터
    cnt = 0  # B가 A를 이긴 횟수
    
    N = len(A)
    
    # 두 리스트의 포인터가 끝에 도달할 때까지 비교
    while a < N and b < N:
        if A[a] < B[b]:  # B가 A보다 크면 이긴다
            cnt += 1
            a += 1  # A의 다음 숫자를 비교하기 위해 포인터 이동
        b += 1  # B의 다음 숫자를 비교하기 위해 포인터 이동
    
    return cnt
