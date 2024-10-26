def solution(dirs):
    # 이동 방향에 따른 좌표 변화 (상, 하, 우, 좌)
    dr = {'U': (-1, 0), 'D': (1, 0), 'R': (0, 1), 'L': (0, -1)}
    
    # 현재 좌표를 (5, 5)로 시작
    di, dj = 5, 5
    
    # 방문한 길을 저장할 set
    v = set()
    
    # 처음 방문한 길 수를 세기 위한 변수
    ans = 0
    
    for d in dirs:
        # 이동할 방향의 변화량을 가져오기
        i, j = dr[d]
        ni, nj = di + i, dj + j
        
        # 새로운 좌표가 0 이상 10 미만의 범위 안에 있는지 확인
        if 0 <= ni <= 10 and 0 <= nj <= 10:
            # 현재 위치에서 새로운 위치로 가는 경로와 반대 경로를 함께 저장
            path = ((di, dj), (ni, nj))
            reverse_path = ((ni, nj), (di, dj))
            
            # 방문하지 않은 길이라면, 양방향 모두 체크 후 추가 -> 점이 아니라 선분이므로
            if path not in v:
                v.add(path)
                v.add(reverse_path)
                ans += 1
            
            # 위치를 업데이트
            di, dj = ni, nj

    return ans
