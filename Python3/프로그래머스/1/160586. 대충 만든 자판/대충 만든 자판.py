import sys

def solution(keymap, targets):
    answer = []
    keys = {}
    
    # 사용해야 할 모든 알파벳 구하기
    target = ''
    for word in targets:
        target += word
    target = ''.join(set(target))

    # 알파벳당 최소 클릭수 구하기
    for t in target:
        min = sys.maxsize
        for i in range(len(keymap)):
            idx = keymap[i].find(t) # 인덱스 찾기
            if idx == -1:
                continue
            if min > idx + 1:
                min = idx + 1
        keys[t] = min

    for i in targets:
        ans = 0
        for j in i:
            ans += keys[j]
        # 인덱스 값이
        if ans >= sys.maxsize:
            ans = -1
        answer.append(ans)
    
    return answer