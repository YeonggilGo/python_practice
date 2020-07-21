T = int(input())


def check_sdoku(board):
    for i in range(9):
        ten = [False] * 9
        for j in range(9):
            if not ten[board[j][i]-1]:
                ten[board[j][i]-1] = True
            else:
                return False

    for i in range(9):
        ten = [False] * 9
        for j in range(9):
            if not ten[board[i][j]-1]:
                ten[board[i][j]-1] = True
            else:
                return False

    for i in range(9):
        ten = [False] * 9
        for j in range(9):
            if not ten[board[(i // 3) * 3 + j // 3][(i % 3) * 3 + j % 3] - 1]:
                ten[board[(i // 3) * 3 + j // 3]
                    [(i % 3) * 3 + j % 3] - 1] = True
            else:
                return False

    return True


for tc in range(1, T + 1):
    board = []
    for i in range(9):
        board.append(list(map(int, input().split())))
    ans = 1 if check_sdoku(board) else 0
    print(f'#{tc} {ans}')
