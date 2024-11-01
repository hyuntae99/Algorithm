# 두 시각의 차이 계산
def time_diff(t1, t2):
    # 시각을 'HH:MM' 형식에서 시간과 분으로 분리
    h1, m1 = map(int, t1.split(':'))
    h2, m2 = map(int, t2.split(':'))
    
    # 분 단위로 변환
    t1 = h1 * 60 + m1
    t2 = h2 * 60 + m2
    
    # 시간 차이 계산
    d = abs(t2 - t1)
    
    return d

# 샵이 붙은 음표를 소문자로 치환
def replace_sharp(note):
    return note.replace('A#', 'a').replace('B#', 'b').replace('C#', 'c').replace('D#', 'd').replace('F#', 'f').replace('G#', 'g')


def solution(m, musicinfos):
    m = replace_sharp(m)
    ans = []
    for music in musicinfos:
        ms = music.split(',')
        s, e, n, lst = ms[0], ms[1], ms[2], ms[3]
        
        d = time_diff(s, e)
        lst = replace_sharp(lst)
        
        mus = ''
        idx = 0
        for i in range(d):
            mus += lst[i%len(lst)]
            if m in mus:
                ans.append((idx,n,d))
                idx += 1
                break

    if not ans:
        return '(None)'
    else:
        ans.sort(key=lambda x: (-x[2], x[0])) 
        return ans[0][1]
        