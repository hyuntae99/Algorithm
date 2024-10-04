def solution(s):
    answer = 0
    # dict
    eng_num = {
        'zero' : '0',
        'one' : '1',
        'two' : '2',
        'three' : '3',
        'four' : '4',
        'five' : '5',
        'six' : '6',
        'seven' : '7',
        'eight' : '8',
        'nine' : '9'
    }
    
    # 같은 문자열을 가지고 있다면 전부 숫자로 대체함
    for eng in eng_num.keys():
        if eng in s:
            s = s.replace(eng, eng_num[eng])
    answer = int(s)
    return answer