# 시계 방향 90도
def rotate(arr,N):
    narr = [x[:] for x in arr]
    for i in range(N):
        for j in range(N):
            narr[i][j] = arr[N-j-1][i]
    return narr

T = int(input())
for test_case in range(1,T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    tarr = []

    print(f'#{test_case}')
    arr1 = rotate(arr,N) # 90도
    tarr.append(arr1)

    arr2 = rotate(arr1,N) # 180도
    tarr.append(arr2)

    arr3 = rotate(arr2,N) # 270도
    tarr.append(arr3)

    for i in range(N):
        for j in range(3):
            print(*tarr[j][i], sep='', end=' ')
        print()
