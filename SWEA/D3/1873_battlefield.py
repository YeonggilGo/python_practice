T = int(input())


def tank_command(s):
    global H, W, tank_dir

    if s == 'U' :
        if pos[0] > 0:
            if board[pos[0] - 1][pos[1]] == '.':
                board[pos[0]][pos[1]] = '.'
                pos[0] -= 1
        board[pos[0]][pos[1]] = '^'
        tank_dir = '^'
    elif s == 'D' :
        if pos[0] < H - 1:
            if board[pos[0] + 1][pos[1]] == '.':
                board[pos[0]][pos[1]] = '.'
                pos[0] += 1
        board[pos[0]][pos[1]] = 'v'
        tank_dir = 'v'
    elif s == 'R' :
        if pos[1] < W - 1:
            if board[pos[0]][pos[1]+1] == '.':
                board[pos[0]][pos[1]] = '.'
                pos[1] += 1
        board[pos[0]][pos[1]] = '>'
        tank_dir = '>'
    elif s == 'L' :
        if pos[1] > 0:
            if board[pos[0]][pos[1]-1] == '.':
                board[pos[0]][pos[1]] = '.'
                pos[1] -= 1
        board[pos[0]][pos[1]] = '<'
        tank_dir = '<'
    elif s == 'S':

        if tank_dir == '>':
            for i in range(pos[1] + 1, W):
                if board[pos[0]][i] == '#':
                    break
                elif board[pos[0]][i] == '*':
                    board[pos[0]][i] = '.'
                    break
        elif tank_dir == '<':
            for i in range(pos[1] - 1, -1, -1):
                if board[pos[0]][i] == '#':
                    break
                elif board[pos[0]][i] == '*':
                    board[pos[0]][i] = '.'
                    break
        elif tank_dir == '^':
            for i in range(pos[0] - 1, -1, -1):
                if board[i][pos[1]] == '#':
                    break
                elif board[i][pos[1]] == '*':
                    board[i][pos[1]] = '.'
                    break
        elif tank_dir == 'v':
            for i in range(pos[0] + 1, H):
                if board[i][pos[1]] == '#':
                    break
                elif board[i][pos[1]] == '*':
                    board[i][pos[1]] = '.'
                    break


data = ''
for tc in range(1, T + 1):
    H, W = map(int, input().split())

    board = []
    for i in range(H):
        board.append(list(input()))

    tank_dir = ''
    for i in range(W):
        for j in range(H):
            if board[j][i] in '><^v':
                tank_dir = board[j][i]
                pos = [j, i]
                break
        if tank_dir:
            break

    len_coms = int(input())
    coms = input()

    for com in coms:
        tank_command(com)

    ans = []
    for line in board:
        tmp = ''.join(line)
        ans. append(tmp)
    data += f'#{tc} '
    print(f'#{tc}', end=' ')


    for each in ans:
        print(each)
        data += f'{each}\n'

    f1 = open('output.txt', 'r')
    output = f1.readlines()

    data = data.split('\n')
    for i in range(len(output)):
        if output[i] != data[i]:
            print(data[i])
            print(output[i])