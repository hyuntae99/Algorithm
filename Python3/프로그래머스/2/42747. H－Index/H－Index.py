def solution(citations):
    c = citations
    for h in range(len(c),-1,-1):
        more = 0
        for compare in c:
            if compare >= h:
                more +=1
        # h번 이상 인용된 논문이 h편 이상이라면
        if more >= h:
            return h