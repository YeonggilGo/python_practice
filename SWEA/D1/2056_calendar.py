thirty_one = [1, 3, 5, 7, 8, 10, 12, [31]]
thirty = [4, 6, 9, 11, [30]]
twenty_eight = [2, [28]]

total_month = [thirty, thirty_one, twenty_eight]

T = int(input())

for tc in range(1, T + 1):
    date = input()
    year = date[:4]
    month = date[4:6]
    day = date[6:]
    ans = 0

    found = False
    for each_month in total_month:
        if int(month) in each_month:
            found = True
            if int(day) > each_month[-1][0]:
                ans = -1
                break

    if not found:
        ans = -1

    if not ans:
        ans = f'{year}/{month}/{day}'

    print(f'#{tc} {ans}')
