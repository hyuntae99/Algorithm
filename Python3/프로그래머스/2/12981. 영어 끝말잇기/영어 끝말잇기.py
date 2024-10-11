def solution(n, words):
    used_words = set() # 사용한 언어
    last_char = words[0][0] # 마지막 알파벳
    
    for idx, word in enumerate(words):
        # 사용했던 단어이거나 끝말이 이어지지 않은 경우
        if word in used_words or word[0] != last_char:
            player = (idx % n) + 1 # 플레이어 순서
            round_number = (idx // n) + 1 # 라운드 
            return [player, round_number]
        used_words.add(word) # 단어 사전에 등록
        last_char = word[-1] # 단어 업데이트
    
    return [0, 0]
