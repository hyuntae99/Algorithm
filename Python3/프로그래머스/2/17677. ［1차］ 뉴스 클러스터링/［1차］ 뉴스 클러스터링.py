import re
from collections import Counter

def solution(str1, str2):
    # 2글자씩 끊어서 다중 집합 만들기
    def make_set(s):
        s = s.lower()
        result = []
        for i in range(len(s)-1):
            if re.match('[a-z]{2}', s[i:i+2]):  # 두 글자가 모두 소문자 알파벳인지 확인
                result.append(s[i:i+2])  # 조건을 만족하면 리스트에 추가
        return result 
    
    set1 = make_set(str1)
    set2 = make_set(str2)
    
    # 각 문자열 집합의 교집합과 합집합 구하기
    counter1 = Counter(set1)
    counter2 = Counter(set2)

    intersection = list((counter1 & counter2).elements())
    union = list((counter1 | counter2).elements())
    
    # 자카드 유사도 계산
    if not union:  
        return 65536
    return int((len(intersection) / len(union)) * 65536)
