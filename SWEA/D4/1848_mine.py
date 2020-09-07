T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    board = [list(input()) for _ in range(N)]
    dy = [-1, -1, 0, 1, 1, 1, 0, -1]
    dx = [0, 1, 1, 1, 0, -1, -1, -1]
    new_board = [[0 for i in range(N)] for j in range(N)]
    visited = [[0 for i in range(N)] for j in range(N)]
    for j in range(N):
        for i in range(N):
            if board[j][i] == '*':
                new_board[j][i] = '*'
                visited[j][i] = 1
                for d in range(8):
                    ny = j + dy[d]
                    nx = i + dx[d]
                    if 0 <= ny < N and 0 <= nx < N and new_board[ny][nx] != '*':
                        new_board[ny][nx] += 1

    ans = 0
    for j in range(N):
        for i in range(N):
            if new_board[j][i] == 0 and visited[j][i] == 0:
                ans += 1
                q = [[j, i]]
                while q:
                    y, x = q.pop()
                    visited[y][x] = 1
                    for d in range(8):
                        ny = y + dy[d]
                        nx = x + dx[d]
                        if 0 <= ny < N and 0 <= nx < N:
                            if new_board[ny][nx] == 0 and visited[ny][nx] == 0:
                                q.append([ny, nx])
                            else:
                                visited[ny][nx] = 1
    ans += sum([line.count(0) for line in visited])
    print(f'#{tc} {ans}')