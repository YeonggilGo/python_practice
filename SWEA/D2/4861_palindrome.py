def is_palindrome(s):
    for l in range(len(s) // 2):
        if s[l] != s[-1 - l]:
            return False
    return True


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    board = []
    for i in range(N):
        board.append(input())

    ans = 0

    # horizontal
    for j in range(N):
        for i in range(N - M + 1):
            if is_palindrome(board[j][i:i+M]):
                ans = board[j][i:i+M]

    # vertical
    if ans:
        pass
    else:
        for i in range(N):
            for j in range(N - M + 1):
                tmp = ''
                for k in range(M):
                    tmp += board[j+k][i]
            if is_palindrome(tmp):
                ans = tmp

    print('#{} {}'.format(tc, ans))
