T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    coms = []
    for _ in range(M):
        coms.append(list(map(int, input().split())))

    board = [[0 for i in range(N)] for j in range(N)]
    board[N // 2][N // 2] = 2
    board[N // 2 - 1][N // 2 - 1] = 2
    board[N // 2][N // 2 - 1] = 1
    board[N // 2 - 1][N // 2] = 1

    dy = [1, 0, -1, 0, 1, 1, -1, -1]
    dx = [0, 1, 0, -1, 1, -1, 1, -1]

    for com in coms:
        pos = [com[1] - 1, com[0] - 1]
        board[pos[0]][pos[1]] = com[2]
        for i in range(8):
            ny = pos[0] + dy[i]
            nx = pos[1] + dx[i]
            if ny >= N or ny < 0 or nx >= N or nx < 0:
                continue
            if board[ny][nx] in [0, com[2]]:
                continue
            else:
                tmp = []
                while board[ny][nx] == (com[2] % 2) + 1:
                    tmp.append((ny,nx))
                    ny += dy[i]
                    nx += dx[i]
                    if ny >= N or ny < 0 or nx >= N or nx < 0:
                        break
                    if board[ny][nx] == com[2]:
                        for stone in tmp:
                            board[stone[0]][stone[1]] = com[2]
                        break
    black = 0
    white = 0
    for i in range(N):
        for j in range(N):
            if board[j][i] == 1:
                black += 1
            elif board[j][i] == 2:
                white += 1

    print(f'#{tc} {black} {white}')
