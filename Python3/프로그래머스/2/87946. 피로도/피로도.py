import itertools
def solution(k, dungeons):
    answer = []
    # 만들 수 있는 모든 경우의 수 
    # 8! = 40320
    cases = list(itertools.permutations(dungeons))

    # 각 케이스에 대해서
    for case in cases:
        cnt = 0 # 입장수
        hp = k # 피로도
        # 각 던전에 대해서
        for dungeon in case:
            # 피로도가 충분하다면
            if hp >= dungeon[0]:
                hp -= dungeon[1] # 피로도 소모
                cnt += 1 # 입장수 추가
            else:
                break
        answer.append(cnt)
            
    return max(answer)