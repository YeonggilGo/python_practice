T = int(input())


def rotate(board):
    res = []
    for i in range(len(board[0])):
        tmp = []
        for j in range(len(board)-1, -1, -1):
            tmp.append(board[j][i])
        res.append(tmp)

    return res


for tc in range(1, T + 1):
    N = int(input())

    num = []
    for i in range(N):
        num.append(list(map(int, input().split())))

    ans = ['']*N
    for i in range(3):
        num = rotate(num)
        for j in range(len(num)):
            ans[j] += ''.join(list(map(str, num[j]))) + ' '

    print(f'#{tc}')
    for i in range(len(ans)):
        print(ans[i])
