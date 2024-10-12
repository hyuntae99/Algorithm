import itertools
# permutations : 순열
# prodcut : 중복 순열
# combinations
# combinations_with_replacement # 중복 조합

def solution(word):
    arr = [] # 만들 수 있는 모든 사전 조합
    words = ['A', 'E', 'I', 'O', 'U'] # 사용 가능한 문자
    
    # 1글자부터 5글자까지의 중복 순열 생성
    for j in range(1, 6):
        for i in itertools.product(words, repeat = j):
            # 생성된 조합을 리스트에 추가
            arr.append(list(i))
    
    # 사전 순서로 정렬
    arr.sort()

    answer = 0
    # 모든 조합을 확인하며 단어를 찾기
    for i in arr:
        answer += 1
        # 리스트를 문자열로 변환하여 비교
        st = ''
        for s in i:
            st += s
        if st == word:
            break
    
    return answer

