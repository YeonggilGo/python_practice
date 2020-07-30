for tc in range(1, int(input()) + 1):
    a, b, c = map(int, input().split())
    if a == b == c:
        ans = a
    else:
        for line in [a, b, c]:
            if [a, b, c].count(line) == 1:
                ans = line
                break
    print(f'#{tc} {ans}')
