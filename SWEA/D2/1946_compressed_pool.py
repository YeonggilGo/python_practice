T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    ans = ''
    for i in range(N):
        info = input().split()
        ans += info[0] * int(info[1])

    print(f'#{tc}')
    cnt = 0
    for letter in ans:
        cnt += 1
        print(letter, end='')
        if cnt == 10:
            cnt = 0
            print()
    print()
