N = int(input())
lst = [0] * (1001)
mx_i, mh, mx = 0, 0, 0
for _ in range(N):
    L, H = map(int, input().split())
    # L위치에 H기록
    lst[L] = H
    # mx_i 구하기
    if mh < H:
        mx_i, mh = L, H
    # 최대 x좌표
    if mx < L:
        mx = L

# 왼쪽부터 처리
ans, mh = 0, 0
for i in range(mx_i+1):
    mh = max(mh, lst[i]) # 지금까지의 최대 높이
    ans += mh

# 오른쪽 처리
mh = 0
for i in range(mx, mx_i, -1):
    mh = max(mh, lst[i]) # 지금까지의 최대 높이
    ans += mh

print(ans)