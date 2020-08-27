for _ in range(10):
    tc = int(input())
    ladder = []
    for i in range(100):
        ladder.append(list(map(int, input().split())))

    for i in range(100):
        if ladder[99][i] == 2:
            pos = [99, i]
            break

    dx = [1, -1]
    while pos[0] != 0:
        for dir in range(2):
            move = False
            nx = dx[dir] + pos[1]
            while 0 <= nx < 100 and ladder[pos[0]][nx]:
                move = True
                nx += dx[dir]
            if move:
                pos[1] = nx - dx[dir]
                break
        pos[0] -= 1

    print(f'#{tc} {pos[1]}')
