for _ in range(10):
    tc = int(input())
    ladder = []
    for i in range(100):
        ladder.append(list(map(int, input().split())))

    start = [[0, i] for i in range(100) if ladder[0][i]]
    end = [[0, i] for i in range(100) if ladder[0][i]]
    res = []
    dx = [1, -1]

    for pos in end:
        cnt = 0
        while pos[0] != 99:
            for dir in range(2):
                move = False
                nx = dx[dir] + pos[1]
                while 0 <= nx < 100 and ladder[pos[0]][nx]:
                    cnt += 1
                    move = True
                    nx += dx[dir]
                if move:
                    pos[1] = nx - dx[dir]
                    break
            pos[0] += 1
        res.append(cnt)

    print(f'#{tc} {start[len(res) - res[::-1].index(min(res)) - 1][1]}')
