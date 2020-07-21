T = int(input())

for tc in range(1, T + 1):
    info = list(map(int, input().split()))

    print(
        f'#{tc} {(info[0]+info[2]+(info[1]+info[3])//60-1)%12+1} {(info[1]+info[3])%60}')
