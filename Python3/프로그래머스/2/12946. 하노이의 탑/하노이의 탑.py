def solution(n):
    answer = []
    
    # 재귀 함수를 통해 하노이의 탑 해결
    def hanoi(n, start, end, mid):
        if n == 1:
            answer.append([start, end])
            return
        # 1. n-1개를 시작에서 중간으로 옮김
        hanoi(n - 1, start, mid, end)
        # 2. 가장 큰 원판을 시작에서 끝으로 옮김
        answer.append([start, end])
        # 3. n-1개를 중간에서 끝으로 옮김
        hanoi(n - 1, mid, end, start)
    
    # 하노이의 탑 시작
    hanoi(n, 1, 3, 2)
    return answer
