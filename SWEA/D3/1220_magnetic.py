for tc in range(1, 11):
    N = int(input())

    board = []
    for _ in range(100):
        board.append(list(map(int, input().split())))

    ans = 0
    can_move = True

    while can_move:
        can_move = False

        # 일단 움직임 먼저
        for i in range(N):
            for j in range(N):

                # N극이 움직임
                if board[j][i] == 1:
                    if j == N - 1:
                        board[j][i] = 0
                        can_move = True
                    elif board[j+1][i] == 0:
                        board[j][i] = 0
                        board[j + 1][i] = 1
                        can_move = True
                    else:
                        pass

                # S극이 움직임
                elif board[j][i] == 2:
                    if j == 0:
                        board[j][i] = 0
                        can_move = True
                    elif board[j-1][i] == 0:
                        board[j][i] = 0
                        board[j - 1][i] = 1
                        can_move = True
                    else:
                        pass

        # 교착상태확인
    for i in range(N):
        for j in range(N-1):

            if board[j][i] == 1 and board[j + 1][i] == 2:
                ans += 1
                board[j][i] = 3
                board[j + 1][i] = 3

    print(f'#{tc} {ans}')
