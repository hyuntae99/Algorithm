from collections import defaultdict

def dfs(idx, score, cal):
    global max_score

    # 목표 칼로리 초과
    if cal > L:
        return

    # 점수를 최대값으로 갱신
    max_score = max(max_score, score)

    # 다음 재료를 탐색
    for i in range(idx + 1, N + 1):
        if not v[i]:
            v[i] = 1
            dfs(i, score + ham[i][0], cal + ham[i][1])
            v[i] = 0


T = int(input())
for test_case in range(1, T + 1):
    # 입력 처리
    N, L = map(int, input().split())

    ham = defaultdict(tuple)
    for i in range(1, N + 1):
        s, c = map(int, input().split())
        ham[i] = (s, c)  # 점수와 칼로리

    # 초기화
    v = [0] * (N + 1)
    max_score = 0

    # DFS 실행
    dfs(0, 0, 0)

    # 결과 출력
    print(f"#{test_case} {max_score}")
