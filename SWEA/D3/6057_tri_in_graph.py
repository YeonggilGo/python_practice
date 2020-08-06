# 시간초과 걸려서

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    l = [[0 for _ in range(N)] for __ in range(N)]
    for _ in range(M):
        tmp = list(map(int, input().split()))
        l[tmp[0] - 1][tmp[1] - 1] = 1
        l[tmp[1] - 1][tmp[0] - 1] = 1
    ans = 0
    for i in range(N):
        for j in range(i + 1, N):
            if l[j][i] == 0:
                continue
            for k in range(j + 1, N):
                if l[k][i] == 0 or l[k][j] == 0:
                    continue
                ans += 1
    print(f'#{tc} {ans}')
    print(l)

# 왜애애애애애애애애애앤지 모르겠지만 이게 더 빨라서 통과가 된다.
# 반복회수는 이게 더 만을텐데 배열의 인덱싱이 더 오래 걸려서 그런갑다..
# 테케는 1000개 N의 최대는 50개
# 각 인덱스가 최대 50개 인데 이게 좀 더 걸리나보다
# 찾아보니까 그냥 bool 배열을 만들어서 인덱싱 한사람도 있고 dfs쓴사람도 있다.

from itertools import combinations as combs

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    l = [[] for _ in range(N)]
    for _ in range(M):
        tmp = sorted(list(map(int, input().split())))
        l[tmp[0] - 1].append(tmp[1] - 1)
    ans = 0
    for comb in combs(range(N), 3):
        if comb[1] in l[comb[0]] and comb[2] in l[comb[0]] and comb[2] in l[comb[1]]:
            ans += 1
    print(f'#{tc} {ans}')
