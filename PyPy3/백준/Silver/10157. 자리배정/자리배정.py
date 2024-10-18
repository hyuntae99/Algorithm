C, R = map(int, input().split())
K = int(input())

# 불가능한 경우
if R*C < K:
    print(0)
else:
    di = [1, 0, -1, 0]
    dj = [0, 1, 0, -1]
    
    # 주변을 1로 둘러싸면: 범위체크 필요 없음 (방문배열이 0,1이므로)
    arr = [[1] * (C+2)] + [[1] + [0]*C + [1] for _ in range(R)] + [[1] * (C+2)]

    ci, cj, dr = 1, 1, 0
    for n in range(1, K):
        arr[ci][cj] = n
        ni, nj = ci + di[dr], cj + dj[dr]
        # 방문x + 범위 내
        if not arr[ni][nj]:
            ci, cj = ni, nj
        else: 
            dr = (dr + 1) % 4  # 방향 꺽기
            ci, cj = ci + di[dr], cj + dj[dr]
    print(f'{cj} {ci}')

