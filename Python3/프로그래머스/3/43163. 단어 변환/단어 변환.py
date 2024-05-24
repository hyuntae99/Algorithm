from collections import deque

def solution(begin, target, words):
    # 타겟이 없는 경우
    if target not in words:
        return 0
    
    word_len = len(begin)
    queue = deque([(begin, 0)]) # 문자열, 카운트
    visited = set()
    visited.add(begin)
    
    while queue:
        current_word, steps = queue.popleft()
        
        # 현재 단어가 타겟과 같다면
        if current_word == target:
            return steps
        
        for i in range(word_len):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                next_word = current_word[:i] + c + current_word[i + 1:]
                
                # 다음 단어가 존재하고 방문하지 않은 단어라면
                if next_word in words and next_word not in visited:
                    visited.add(next_word) # 방문 처리
                    queue.append((next_word, steps + 1)) # 다음 문자열, 카운트 추가
    
    return 0
