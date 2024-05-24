def solution(N, number):
    # DP 테이블 초기화
    dp = [set() for _ in range(9)]
    
    # N, NN, NNN, ... NNNNNNNN을 dp[i]에 추가
    for i in range(1, 9):  
        dp[i].add(int(str(N) * i)) 
        
    # DP 탐색
    for i in range(1, 9):  # i = 횟수
        for j in range(1, i):  # j는 1부터 i-1까지 반복
            for x in dp[j]:  # dp[j]의 모든 원소 x에 대해
                for y in dp[i - j]:  # dp[i-j]의 모든 원소 y에 대해
                    dp[i].add(x + y)  # x + y를 dp[i]에 추가
                    dp[i].add(x - y)  # x - y를 dp[i]에 추가
                    dp[i].add(x * y)  # x * y를 dp[i]에 추가
                    if y != 0:  
                        dp[i].add(x // y)  # x // y를 dp[i]에 추가
                    if x != 0:
                        dp[i].add(y // x)  # y // x를 dp[i]에 추가
        
        # 타겟 넘버 발견 시 최소 연산 횟수 반환
        if number in dp[i]:
            return i  
    return -1
