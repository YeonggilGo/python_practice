T = int(input())

for tc in range(1, T + 1):
    N = input()

    now = 0
    see = [False] * 10

    while False in see:
        now = str(int(now)+int(N))
        for each in now:
            see[int(each)] = True

    print(f'#{tc} {now}')
