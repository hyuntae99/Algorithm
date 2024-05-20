def solution(park, routes):
    answer = []
    x, y = 0, 0
    
    # 시작 좌표 찾기
    for i in range(len(park)):
        if 'S' in park[i]:
            y, x = i, park[i].index('S')
            break

    # 배열의 크기
    n_y = len(park)
    n_x = len(park[0])

    for route in routes:
        # 방향과 크기
        direction, power = route.split()
        power = int(power)
        
        if direction == 'N':
            if y - power >= 0 and all(park[y - i][x] != 'X' for i in range(1, power + 1)):
                y -= power
        elif direction == 'S':
            if y + power < n_y and all(park[y + i][x] != 'X' for i in range(1, power + 1)):
                y += power
        elif direction == 'W':
            if x - power >= 0 and all(park[y][x - i] != 'X' for i in range(1, power + 1)):
                x -= power
        elif direction == 'E':
            if x + power < n_x and all(park[y][x + i] != 'X' for i in range(1, power + 1)):
                x += power
    
    answer = [y, x]
    return answer
