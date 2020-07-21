T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    vel = 0
    pos = 0

    for i in range(N):
        info = input()
        if info == '0':
            pos += vel
        else:
            info_com, info_vel = map(int, info.split())
            if info_com == 1:
                vel += info_vel
                pos += vel
            else:
                vel -= info_vel
                if vel < 0:
                    vel = 0
                pos += vel

    print(f'#{tc} {pos}')
