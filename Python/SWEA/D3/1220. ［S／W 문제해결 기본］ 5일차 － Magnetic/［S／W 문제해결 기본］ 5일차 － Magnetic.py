T = 10
for test_case in range(1, T+1):
    N = int(input())  # 테이블의 크기 (항상 100)
    lst = []

    for _ in range(N):
        tmp = list(map(int, input().split()))
        lst.append(tmp)

    ans = 0

    # 테이블의 각 열을 처리
    for j in range(N):  # 열 단위로 순회
        state = 0  # 현재 상태를 나타내는 변수 (N극 상태를 추적)
        for i in range(N):  # 행 단위로 순회
            if lst[i][j] == 1:  # N극 자성체를 발견한 경우
                state = 1  # N극 상태로 설정
            elif lst[i][j] == 2 and state == 1:  # S극 자성체를 만나고, 이전에 N극 상태였던 경우
                ans += 1  # 교착 상태를 카운트
                state = 0  # 상태를 초기화

    print(f"#{test_case} {ans}")
