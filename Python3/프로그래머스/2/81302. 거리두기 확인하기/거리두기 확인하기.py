def solution(places):
    def f1(i, j):
        # 바로 오른쪽에 사람이 있을 때
        if j < M-1 and place[i][j+1] == 'P':
            return 0
        # 두 칸 오른쪽에 사람이 있을 때 (파티션 없이)
        elif j < M-2 and place[i][j+2] == 'P' and place[i][j+1] != 'X':
            return 0
        return 1

    def f2(i, j):
        # 바로 아래 사람이 있을 때
        if i < N-1 and place[i+1][j] == 'P':
            return 0
        # 두 칸 아래 사람이 있을 때 (파티션 없이)
        elif i < N-2 and place[i+2][j] == 'P' and place[i+1][j] != 'X':
            return 0
        return 1

    def f3(i, j):
        # 대각선 아래 오른쪽에 사람이 있을 때
        if i < N-1 and j < M-1 and place[i+1][j+1] == 'P':
            # 사이에 책상이 없다면 부적격
            if place[i+1][j] != 'X' or place[i][j+1] != 'X':
                return 0
        return 1

    def f4(i, j):
        # 대각선 아래 왼쪽에 사람이 있을 때
        if i < N-1 and j >= 1 and place[i+1][j-1] == 'P':
            # 사이에 책상이 없다면 부적격
            if place[i+1][j] != 'X' or place[i][j-1] != 'X':
                return 0
        return 1

    ans = []
    for place in places:
        N, M = len(place), len(place[0])
        res = set()
        for i in range(N):
            for j in range(M):
                if place[i][j] == 'P':
                    # 1. 오른쪽
                    res.add(f1(i, j))
                    # 2. 아래
                    res.add(f2(i, j))
                    # 3. 대각선 오른쪽 아래
                    res.add(f3(i, j))
                    # 4. 대각선 왼쪽 아래
                    res.add(f4(i, j))

        # 부적격 판정이 있을 경우
        if 0 in res:
            ans.append(0)
        else:
            ans.append(1)

    return ans
