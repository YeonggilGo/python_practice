T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    maze = []
    for _ in range(N):
        maze.append(list(map(int, list(input()))))
    for j in range(N):
        for i in range(N):
            if maze[j][i] == 3:
                end = [j, i]
            elif maze[j][i] == 2:
                start = [j, i]
    dy = [1, -1, 0, 0]
    dx = [0, 0, -1, 1]
    visited = [[0 for j in range(N)] for i in range(N)]
    q = [start]
    ans = 0
    while q:
        y, x = q.pop()
        if [y, x] == end:
            ans = 1
            break

        visited[y][x] = 1
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < N and 0 <= nx < N:
                if maze[ny][nx] != 1 and not visited[ny][nx]:
                    q.append([ny, nx])

    print(f'#{tc} {ans}')
