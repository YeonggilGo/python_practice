# dfs는 시간초과가 걸린다. 테케가 10000개인걸 봤으면 dfs로 시간낭비를
# 안했을꺼다. 조건먼저 잘 살펴보자
# 인줄 알았는데 dfs가 맞았다. 일단 조건을 여러가지 주고 간단한 동작의
# dfs는 그렇게 느리지 않다. 조건만 잘 생각하면 되는 문제였다.

piece = ['00', '01', '10', '11']


def dfs(bi, A, B, C, D):
    global ans
    if ans != 'impossible':
        return
    if abs(B - C) > 1:
        return
    if A < 0 or B < 0 or C < 0 or D < 0:
        return
    if A + B + C + D == 0:
        ans = bi
        return
    if bi[-1] == '0':
        dfs(bi + '0', A - 1, B, C, D)
        dfs(bi + '1', A, B - 1, C, D)
        return
    else:
        dfs(bi + '0', A, B, C - 1, D)
        dfs(bi + '1', A, B, C, D - 1)
        return


T = int(input())

for tc in range(1, T + 1):
    A, B, C, D = map(int, input().split())
    ans = 'impossible'
    dfs('0', A, B, C, D)
    dfs('1', A, B, C, D)
    print(f'#{tc} {ans}')
