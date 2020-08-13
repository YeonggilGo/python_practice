from collections import deque

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]
for _ in range(1, 11):
    tc = int(input())
    maze = []
    for i in range(100):
        maze.append(list(map(int, input())))

    # 시작, 출발점 찾기
    for i in range(100):
        for j in range(100):
            if maze[j][i] == 2:
                start = [j, i]
            elif maze[j][i] == 3:
                end = [j, i]
    ans = 0
    visited = [[0 for i in range(100)] for j in range(100)]

    q = deque([start])
    while q:
        pos = q.popleft()
        if pos == end:
            ans = 1
            break
        visited[pos[0]][pos[1]] = 1
        for i in range(4):
            ny = pos[0] + dy[i]
            nx = pos[1] + dx[i]
            if 0 <= ny < 100 and 0 <= nx < 100 and not visited[ny][nx]:
                if maze[ny][nx] != 1:
                    q.append([ny, nx])

    print(f'#{tc} {ans}')
