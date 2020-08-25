from collections import deque


# check : check that program can end for each endpoint
def check():
    end = 0
    end_points = []
    for j in range(R):
        for i in range(C):
            if program[j][i] == '@':
                end += 1
                end_points.append([j, i])
    if end < 1:
        return False
    bad_point = 0

    for end_point in end_points:
        # check top and bottom
        for i in range(2):
            pos = [(end_point[0] + dy[i]) % R, (end_point[1] + dx[i]) % C]
            if program[pos[0]][pos[1]] in ['<', '>']:
                bad_point += 1
        for i in range(2, 4):
            pos = [(end_point[0] + dy[i]) % R, (end_point[1] + dx[i]) % C]
            if program[pos[0]][pos[1]] in ['^', 'v']:
                bad_point += 1
    end -= bad_point
    if end < 1:
        return False
    return True


def action(command):
    global dir_idx, mem, ans
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
    elif command == '@':
        ans = 'YES'
        return
    elif command.isdigit():
        mem = int(command)
    elif command == '+':
        if mem == 15:
            mem = 0
        else:
            mem += 1
    elif command == '-':
        if mem == 0:
            mem = 15
        else:
            mem -= 1


if __name__ == '__main__':
    T = int(input())
    for tc in range(1, T + 1):
        R, C = map(int, input().split())
        dy = [-1, 1, 0, 0]
        dx = [0, 0, -1, 1]

        program = []
        for i in range(R):
            program.append(input())

        ans = 'NO'
        if check():
            visited = [[[] for i in range(C)] for j in range(R)]
            q = deque([[[0, 0], 3, 0]])
            while q:
                pos, dir_idx, mem = q.popleft()

                visited[pos[0]][pos[1]].append([dir_idx, mem])
                command = program[pos[0]][pos[1]]

                if command == '?':
                    for i in range(4):
                        new_pos = [(pos[0] + dy[i]) % R, (pos[1] + dx[i]) % C]
                        if [i, mem] not in visited[new_pos[0]][new_pos[1]]:
                            q.append([new_pos, dir_idx, mem])
                else:
                    action(command)
                    new_pos = [(pos[0] + dy[dir_idx]) % R, (pos[1] + dx[dir_idx]) % C]
                    if [dir_idx, mem] not in visited[new_pos[0]][new_pos[1]]:
                        q.append([new_pos, dir_idx, mem])

        print(f'#{tc} {ans}')
