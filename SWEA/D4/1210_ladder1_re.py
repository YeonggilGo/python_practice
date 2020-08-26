if __name__ == '__main__':
    for _ in range(10):
        tc = int(input())
        ladder = []
        for i in range(100):
            ladder.append(list(map(int, input().split())))

        # end : end point
        for i in range(100):
            if ladder[99][i] == 2:
                end = (99, i)
                break

        # q: a list to store the next moveable location
        q = [end]

        # dy, dx : list pointing next direction, don't need to move downward
        dy = [-1, 0, 0]
        dx = [0, -1, 1]

        # start from the end point, find the route to location of which y coordinate is 0
        while q:
            # if there is more than moveable location,
            if len(q) <= 1:
                pos = q.pop()
            else:
                ny,nx = q.pop()
                dir_x = nx-q[0][1]
                q = []
                while True:
                    if 0<=nx+dir_x<100 and ladder[ny][nx + dir_x]:
                        nx += dir_x
                    else:
                        break
                ny -= 1
                q.append((ny,nx))
                continue

            if pos[0] == 0:
                break

            for i in range(3):
                ny = pos[0] + dy[i]
                nx = pos[1] + dx[i]
                if 0 <= ny < 100 and 0 <= nx < 100:
                    if ladder[ny][nx]:
                        q.append((ny, nx))

        print('#{} {}'.format(tc, pos[1]))
