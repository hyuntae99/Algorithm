def solution(name):
    # 모든 문자가 'A'인 경우 조작이 필요 없으므로 0을 반환
    if set(name) == {'A'}:
        return 0

    a_pos = ord('A')  # 'A' : 65
    z_pos = ord('Z')  # 'Z' : 90

    answer = float('inf')  # 초기 값을 무한대로 설정

    # name의 절반 길이까지 반복 (좌우 대칭을 고려하여 절반까지만 체크)
    for i in range(len(name) // 2 + 1):
        l_r = name[-i:] + name[:-i]  # 왼쪽 먼저 갔다가 오른쪽으로 이동
        r_l = name[i: :-1] + name[i+1:][::-1]  # 기준점에서 반대로 갔다가 다시 좌측으로 이동
        
        # 왼쪽 먼저 이동하는 경우와 오른쪽 먼저 이동하는 경우를 비교
        for n in [l_r, r_l]:
            # 끝에 있는 'A'는 셀 필요 없으므로 제거
            while n and n[-1] == 'A':
                n = n[:-1]
                
            # 각 문자를 'A'로 바꾸기 위해 필요한 조작 횟수를 계산
            cnt = [min(ord(c) - a_pos, (z_pos + 1) - ord(c)) for c in n]
            
            # 이동 횟수 (i) + 알파벳 변경 횟수 (len(cnt)-1 + sum(cnt))의 최소값을 갱신
            answer = min(answer, i + (len(cnt) - 1) + sum(cnt))

    return answer
