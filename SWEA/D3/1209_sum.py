for _ in range(10):
    t = int(input())

    board = []
    for i in range(100):
        board.append(list(map(int, input().split())))

    ans = 0

    for i in range(100):
        ans = ans if ans > sum(board[i]) else sum(board[i])

    for i in range(100):
        tmp = 0
        for j in range(100):
            tmp += board[j][i]

        ans = ans if ans > tmp else tmp

    tmp = 0
    tmp2 = 0
    for i in range(100):
        tmp += board[i][i]
        tmp2 += board[i][-i - 1]

    ans = ans if ans > max(tmp, tmp2) else max(tmp, tmp2)

    print(f'#{t} {ans}')
