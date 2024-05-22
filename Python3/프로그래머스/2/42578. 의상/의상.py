def solution(clothes):
    answer = 1
    # 옷 종류에 대한 가짓수
    closet = {c[1] : 0 for c in clothes}
    for c in clothes:
        closet[c[1]] += 1

    # 옷 종류에 대해서 모두 곱한다.
    for n in closet.values():
        answer *= (n + 1) # 안입는 경우
    answer -= 1 # 아무것도 안입은 경우 제외
    return answer