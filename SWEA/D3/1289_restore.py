T = int(input())

for tc in range(1, T + 1):
    tar = input()
    ans = 0
    my = '0' * len(tar)
    pos = 0
    while tar != my:
        if tar[pos] != my[pos]:
            my = my[:pos] + str((int(my[pos]) + 1) % 2) * (len(tar) - pos)
            ans += 1
            pos += 1
        else:
            pos += 1

    print(f'#{tc} {ans}')
