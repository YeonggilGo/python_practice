if __name__ == '__main__':
    for tc in range(1, int(input()) + 1):
        V, E = map(int, input().split())

        # MAP : each element is a list that store movable points
        MAP = [[] for _ in range(V + 1)]
        for i in range(E):
            tmp = list(map(int, input().split()))
            MAP[tmp[0]].append(tmp[1])

        S, T = map(int, input().split())
        flag = 0

        # q : list stored movable points, start from 'S'
        q = [S]
        visited = [False] * (V + 1)
        while q:
            pos = q.pop()

            # end
            if pos == T:
                flag = 1
                break

            visited[pos] = True

            # points which are movable and not visited append to 'q'
            for next_pos in MAP[pos]:
                if next_pos not in visited:
                    q.append(next_pos)

        print('#{} {}'.format(tc, flag))