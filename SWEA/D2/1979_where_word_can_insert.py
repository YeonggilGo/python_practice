def check(pos):
    global ans, N, K

    # 가로
    if pos[1] == 0:
        if board[pos[0]][pos[1]:pos[1] + K].count(1) == K and board[pos[0]][pos[1] + K] == 0:
            ans += 1
    elif pos[1] == N - K:
        if board[pos[0]][pos[1]:pos[1]+K].count(1) == K and board[pos[0]][pos[1] - 1] == 0:
            ans += 1
    else:
        if board[pos[0]][pos[1]: pos[1] + K].count(1) == K and board[pos[0]][pos[1] + K] == 0 and board[pos[0]][pos[1] - 1] == 0:
            ans += 1

    # 세로
    tmp = [board[i][pos[1]] for i in range(N)]
    if pos[0] == 0:
        if tmp[:K].count(1) == K and tmp[K] == 0:
            ans += 1
    elif pos[0] == N - K:
        if tmp[pos[0]: pos[0] + K].count(1) == K and tmp[pos[0] - 1] == 0:
            ans += 1
    else:
        if tmp[pos[0]: pos[0] + K].count(1) == K and tmp[pos[0] - 1] == 0 and tmp[pos[0] + K] == 0:
            ans += 1


T = int(input())

for tc in range(1, T + 1):
    ans = 0
    N, K = map(int, input().split())

    board = []
    for i in range(N):
        board.append(list(map(int, input().split())))

    for i in range(N):
        for j in range(N):
            check([j, i])

    print(f'#{tc} {ans}')
