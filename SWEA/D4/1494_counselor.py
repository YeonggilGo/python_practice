def sol(idx, plus, minus, x, y):
    global ans
    if idx == N:
        ans = min(ans, x ** 2 + y ** 2)
        return
    else:
        if plus < N // 2:
            sol(idx + 1, plus + 1, minus, x + pos[idx][0], y + pos[idx][1])
        if minus < N // 2:
            sol(idx + 1, plus, minus + 1, x - pos[idx][0], y - pos[idx][1])


for tc in range(1, int(input()) + 1):
    N = int(input())
    pos = []
    for i in range(N):
        pos.append(list(map(int, input().split())))

    ans = 999999999999999

    # 미리 하나를 넣어주어도 상관없다. 시간을 반으로 단축시킬 수 있다.
    sol(1,1,0,pos[0][0],pos[0][1])
    print(f'#{tc} {ans}')