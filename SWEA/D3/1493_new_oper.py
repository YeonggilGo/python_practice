def hash(a, b):
    return sum(range(1, a + b)) - b + 1


def ampersand(n):
    cnt = 0
    while sum(range(cnt)) < n:
        cnt += 1
    tmp = sum(range(cnt))
    return (cnt - (tmp-n + 1), tmp-n + 1)


T = int(input())

for tc in range(1, T + 1):
    a, b = map(int, input().split())

    a, b = ampersand(a), ampersand(b)
    ans = hash(a[0]+b[0], a[1]+b[1])

    print(f'#{tc} {ans}')
