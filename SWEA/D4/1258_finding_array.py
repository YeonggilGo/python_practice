T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    board = []
    for _ in range(N):
        board.append(list(map(int, input().split())))

    arr = []
    visited = [[0 for i in range(N)] for j in range(N)]

    for i in range(N):
        for j in range(N):
            if visited[j][i]:
                continue
            visited[j][i] = 1

            if board[j][i]:
                y = j
                x = i
                while y < N and board[y][i]:
                    y += 1
                while x < N and board[j][x]:
                    x += 1
                arr.append([y - j, x - i])
                for b in range(j, y):
                    for a in range(i, x):
                        visited[b][a] = 1

    arr.sort(key = lambda x: (x[0] * x[1], x[0]))
    print(f'#{tc} {len(arr)}', end = ' ')
    for line in arr:
        print(*line,end = ' ')
    print()