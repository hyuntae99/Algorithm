def solution(msg):
    # 초기 사전 만들기
    dictionary = {chr(i + 65): i + 1 for i in range(26)}
    answer = []
    idx = 27
    i = 0
    
    while i < len(msg):
        w = msg[i]
        # 가장 긴 패턴을 찾기
        while i + 1 < len(msg) and w + msg[i + 1] in dictionary:
            i += 1
            w += msg[i]
        
        # 결과 저장
        answer.append(dictionary[w])
        
        # 사전에 새 패턴 추가
        if i + 1 < len(msg):
            dictionary[w + msg[i + 1]] = idx
            idx += 1
        
        i += 1
    
    return answer
