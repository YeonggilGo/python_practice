def check_enable():
    global end
    '''
    Check all the end points can access from near
    :return:boolean
    '''
    # '@' doesn't exist
    if end < 1:
        return False

    bad_points = 0
    for end_point in end_points:
        # check top & bottom
        for i in range(2):
            ny, nx = move(i, end_point)
            if program[ny][nx] in ['>', '<']:
                bad_points += 1
            else:
                bad_points = 0
                break
        # check side
        for i in range(2, 4):
            ny, nx = move(i, end_point)
            if program[ny][nx] in ['^', 'v']:
                bad_points += 1
            else:
                bad_points = 0
                break

    end -= bad_points
    if end < 1:
        return False
    return True


def move(dir_idx, pos):
    return [(pos[0] + dy[dir_idx]) % R, (pos[1] + dx[dir_idx]) % C]


def action(dir_idx, mem, pos):
    global ans
    while pos:
        command = program[pos[0]][pos[1]]
        if command == '@':
            return 1
        if [dir_idx, mem] in visited[pos[0]][pos[1]]:
            return 0
        visited[pos[0]][pos[1]].append([dir_idx, mem])

        if command == '?':
            for i in range(4):
                if action(i, mem, move(i, pos)):
                    return 1
        else:
            if command == '<':
                dir_idx = 2
            elif command == '>':
                dir_idx = 3
            elif command == '^':
                dir_idx = 0
            elif command == 'v':
                dir_idx = 1
            elif command == '_':
                if mem == 0:
                    dir_idx = 3
                else:
                    dir_idx = 2
            elif command == '|':
                if mem == 0:
                    dir_idx = 1
                else:
                    dir_idx = 0
            elif command == '.':
                pass
            elif command.isdigit():
                mem = int(command)
            elif command == '+':
                mem = (mem + 1) % 16
            elif command == '-':
                mem = (mem - 1) % 16
            pos = move(dir_idx, pos)


if __name__ == '__main__':
    T = int(input())
    for tc in range(1, T + 1):
        R, C = map(int, input().split())
        dy = [-1, 1, 0, 0]
        dx = [0, 0, -1, 1]
        program = []
        for i in range(R):
            program.append(input())

        # find end points
        end_points = []
        for j in range(R):
            for i in range(C):
                if program[j][i] == '@':
                    end_points.append((j, i))
        end = len(end_points)

        if check_enable():
            visited = [[[] for i in range(C)] for j in range(R)]
        res = 'YES' if action(3,0, [0,0]) else 'NO'
        print(f'#{tc} {res}')
