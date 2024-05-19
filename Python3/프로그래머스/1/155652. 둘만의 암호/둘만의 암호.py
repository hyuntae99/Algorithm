# 하나씩 증가하는 함수
def rotate(aci):
    # 97 = 'a', 알파벳은 26개
    return (aci - 96) % 26 + 97

def solution(s, skip, index):
    answer = ''

    for c in s:        
        aci = ord(c)
        for i in range(index):
            aci = rotate(aci)
            if chr(aci) in skip:
                aci = rotate(aci)
            # skip 문자열에 포함된 문자는 건너뛰기
            while chr(aci) in skip:
                aci = rotate(aci)
        answer += chr(aci)

    return answer