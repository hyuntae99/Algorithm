def solution(wallpaper):
    answer = []
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[i])):
            if wallpaper[i][j] == '#':
                answer.append([i + 1, j + 1])
    
    lux, luy = answer[0][0] - 1, answer[0][1] - 1
    rdx, rdy = 0, 0
    for ans in answer:
        print(ans)
        if lux >= ans[0]:
            lux = ans[0] - 1
        if luy >= ans[1]:
            luy = ans[1] - 1
        if ans[0] > rdx:
            rdx = ans[0]
        if ans[1] > rdy:
            rdy = ans[1]
    
    reulst = [lux, luy, rdx, rdy]
        
    return reulst