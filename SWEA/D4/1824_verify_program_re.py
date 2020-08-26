def check_enable():
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
            ny = end_point[0] + dy[i]
            nx = end_point[1] + dx[i]
            if program[ny][nx] in ['>','<']:
                bad_points += 1
        # check side
        for i in range(2,4):
            ny = end_point[0] + dy[i]
            nx = end_point[1] + dx[i]
            if program[ny][nx] in ['^','v']:
                bad_points += 1

        # this point!!




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
                    end_points.append((j,i))
        end = len(end_points)
