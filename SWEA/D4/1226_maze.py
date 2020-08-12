def dfs(pos):
    global ans
    if maze[pos[0]][pos[1]] == 3:
        ans = 1
        return

    visited[pos[0]][pos[1]] = 1
    for i in range(4):
        ny = pos[0] + dy[i]
        nx = pos[1] + dx[i]
        if 0 <= ny < 16 and 0 <= nx < 16 and not visited[ny][nx]:
            if maze[ny][nx] != 1:
                dfs([ny, nx])
    visited[pos[0]][pos[1]] = 0


dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]
for _ in range(1, 11):
    tc = int(input())
    maze = []
    for i in range(16):
        maze.append(list(map(int, input())))

    # 시작, 출발점 찾기
    for i in range(16):
        for j in range(16):
            if maze[j][i] == 2:
                start = [j, i]
            elif maze[j][i] == 3:
                end = [j, i]
    ans = 0
    visited = [[0 for i in range(16)] for j in range(16)]
    dfs(start)
    print(f'#{tc} {ans}')
