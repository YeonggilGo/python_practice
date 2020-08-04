thirty = [4, 6, 9, 11, 30]
thirtyOne = [1, 3, 5, 7, 8, 10, 12, 31]
twentyNine = [2, 29]
months = [twentyNine, thirty, thirtyOne]
first = 0

T = int(input())
for tc in range(1, T + 1):
    m, d = map(int, input().split())
    ans = 4
    for i in range(1, m + 1):
        if m == i:
            ans += d - 1
        else:
            for month in months:
                if i in month:
                    ans += month[-1]
    ans %= 7
    print(f'#{tc} {ans}')