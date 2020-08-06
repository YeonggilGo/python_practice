T = int(input())
for tc in range(1, T + 1):
    board = [[0 for i in range(10)] for j in range(10)]
    coms = []
    N = int(input())
    for _ in range(N):
        coms.append(list(map(int, input().split())))

    ans = 0
    for com in coms:
        for i in range(com[0], com[2] + 1):
            for j in range(com[1], com[3] + 1):
                if board[j][i] in [1, 2]:
                    if board[j][i] != com[4]:
                        ans += 1
                        board[j][i] = 3
                elif board[j][i] == 0:
                    board[j][i] = com[4]

    print('#{} {}'.format(tc, ans))
