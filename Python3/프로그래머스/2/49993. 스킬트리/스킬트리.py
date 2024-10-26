def solution(skill, skill_trees):
    cnt = 0
    for skills in skill_trees:
        prev = ''
        flag = True
        for s in skills:
            l = skill.find(s) + 1 # 필요 길이
            
            # 존재한다면 추가
            if l > 0:
                prev += s
            else:
                continue
            
            # 지금까지의 스킬트리가 유효하지 않다면 종료
            if not skill.startswith(prev):
                flag = False
                break
                
        # 무사히 통과했다면
        if flag:
            cnt += 1
    
    return cnt