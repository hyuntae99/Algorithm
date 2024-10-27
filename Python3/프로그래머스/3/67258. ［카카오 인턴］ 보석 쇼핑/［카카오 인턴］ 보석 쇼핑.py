from collections import Counter

def solution(gems):
    gem_types = len(set(gems))  # 모든 보석 종류의 개수
    counter = Counter()  # 현재 구간 내 보석들의 개수를 저장할 Counter
    start, end = 0, 0  # 슬라이딩 윈도우의 시작과 끝
    answer = [0, len(gems)]  # 정답 구간의 시작과 끝을 저장할 변수 (최소 구간)
    
    # 끝점 설정 + counter 등록
    while end < len(gems):
        counter[gems[end]] += 1
        end += 1

        # 모든 보석 종류를 포함하고 있다면
        while len(counter) == gem_types:
            # 기존 구간 길이보다 작다면 갱신
            if end - start < answer[1] - answer[0]:
                answer = [start, end]  # index로 변환하여 저장

            counter[gems[start]] -= 1  # 시작점의 보석 개수 감소
            if counter[gems[start]] == 0:  # 해당 보석 개수가 0이 되면 제거
                del counter[gems[start]]
            start += 1  # 시작점 이동

    # idx기준이 아니므로
    answer[0] += 1
    return answer
