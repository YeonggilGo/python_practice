def rotate_key(key, M):
    temp_key = []
    for i in range(M):
        temp = []
        for j in range(M - 1, -1, -1):
            temp.append(key[j][i])
        temp_key.append(temp)
    return temp_key


def move_key(grooves, j, i, N):
    return [(g[0] + j, g[1] + i) for g in grooves if N > g[0] + j >= 0 and N > g[1] + i >= 0]


def solution(key, lock):
    answer = False
    N, M = len(lock), len(key)
    holes = [(j, i) for i in range(N) for j in range(N) if not lock[j][i]]

    for _ in range(4):
        grooves = [(j, i) for i in range(M) for j in range(M) if key[j][i]]
        for j in range(-M + 1, N):
            for i in range(-M + 1, N):
                new_grooves = move_key(grooves, j, i, N)
                if set(new_grooves) == set(holes):
                    answer = True
                    break
            if answer: break
        if answer:
            break
        else:
            key = rotate_key(key, M)
    return answer
