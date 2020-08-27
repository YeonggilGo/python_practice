if __name__ == '__main__':
    for _ in range(10):
        tc = int(input())
        ladder = []
        for i in range(100):
            ladder.append(list(map(int, input().split())))

        start_points = [[0, i] for i in range(100) if ladder[0][i]]

        dx = [1, -1]
        min_cnt = 10000
        res = -1
        for pos in start_points:
            cnt = 0
            start = pos[1]
            while pos[0] != 99:
                for dir in range(2):
                    movable_side = False
                    nx = dx[dir] + pos[1]
                    while 0 <= nx < 100 and ladder[pos[0]][nx]:
                        cnt += 1
                        movable_side = True
                        nx += dx[dir]
                    if movable_side:
                        pos[1] = nx - dx[dir]
                        break
                pos[0] += 1
                cnt += 1
            if min_cnt > cnt:
                min_cnt = cnt
                res = start

        print('#{} {}'.format(tc, res))
