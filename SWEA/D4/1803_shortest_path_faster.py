from collections import deque

if __name__ == '__main__':
    T = int(input())
    for tc in range(1, T + 1):
        N, M, S, E = map(int, input().split())
        route = {}
        for i in range(M):
            tmp = list(map(int, input().split()))
            if tmp[0] in route:
                route[tmp[0]].append([tmp[1], tmp[2]])
            else:
                route[tmp[0]] = [[tmp[1], tmp[2]]]
            if tmp[1] in route:
                route[tmp[1]].append([tmp[0], tmp[2]])
            else:
                route[tmp[1]] = [[tmp[0], tmp[2]]]

        dp = [-1] * (N + 1)
        dp[S] = 0
        q = deque([[S, 0]])
        while q:
            pos = q.popleft()
            for next_pos in route[pos[0]]:
                if dp[next_pos[0]] == -1 or dp[next_pos[0]] > pos[1] + next_pos[1]:
                    dp[next_pos[0]] = pos[1] + next_pos[1]
                    q.append([next_pos[0],pos[1] + next_pos[1]])

        print(f'#{tc} {dp[E]}')
