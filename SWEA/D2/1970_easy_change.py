T = int(input())

for tc in range(1, T + 1):
    money = int(input())
    change = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    ans = [0] * len(change)

    for i in range(len(change)):
        if money // change[i] >= 1:
            ans[i] += money//change[i]
            money %= change[i]

    print(f'#{tc}')
    ans = ' '.join(list(map(str, ans)))
    print(ans)
