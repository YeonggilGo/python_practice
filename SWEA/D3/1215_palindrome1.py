def is_palin(list_):
    for i in range(len(list_) // 2):
        if list_[i] != list_[-i - 1]:
            return False
    return True


def rotate(board):
    res = []
    for i in range(len(board[0])):
        tmp = []
        for j in range(len(board)-1, -1, -1):
            tmp.append(board[j][i])
        res.append(tmp)

    return res


for tc in range(1, 11):
    N = int(input())
    ans = 0
    board = []
    for i in range(8):
        board.append(input())

    # 가로
    for i in range(8 - N + 1):
        for j in range(8):
            if is_palin(board[j][i:i + N]):
                ans += 1

    board = rotate(board)

    # 세로
    for i in range(8 - N + 1):
        for j in range(8):
            if is_palin(board[j][i:i + N]):
                ans += 1
    print(f'#{tc} {ans}')
