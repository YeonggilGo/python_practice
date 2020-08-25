def is_palin(list_):
    for i in range(len(list_) // 2):
        if list_[i] != list_[-i - 1]:
            return False
    return True


for tc in range(1, 11):
    N = int(input())
    board = []
    for i in range(100):
        board.append(input())
    ans = 0
    for k in range(100, 1, -1):
        if ans:
            break

        # 가로
        for i in range(100 - k + 1):
            double_break = False
            for j in range(100):
                if is_palin(board[j][i:i + k]):
                    ans = k
                    double_break = True
                    break
            if double_break:
                break

        # 세로
        if ans:
            break
        for j in range(100 - k + 1):
            double_break = False
            for i in range(100):
                tmp = ''
                for l in range(k):
                    tmp += board[j + l][i]

                if is_palin(tmp):
                    ans = k
                    double_break = True
                    break
            if double_break:
                break

    print(f'#{tc} {ans}')
