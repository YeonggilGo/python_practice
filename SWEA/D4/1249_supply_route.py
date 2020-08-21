from collections import deque

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

T = int(input())
for tc in range(1, 11):
    N = int(input())
    board = []
    for i in range(N):
        board.append(list(map(int, input())))
    dp = [[-1 for i in range(N)] for j in range(N)]
    dp[0][0] = board[0][0]

    q = deque([[0, 0]])
    while q:
        pos = q.popleft()
        if pos == [N - 1, N - 1]:
            continue
        current_v = dp[pos[0]][pos[1]]
        for i in range(4):
            ny = pos[0] + dy[i]
            nx = pos[1] + dx[i]
            if 0 <= ny < N and 0 <= nx < N:
                if dp[ny][nx] == -1 or current_v + board[ny][nx] < dp[ny][nx]:
                    dp[ny][nx] = current_v + board[ny][nx]
                    q.append([ny, nx])
    print(f'#{tc} {dp[-1][-1]}')
