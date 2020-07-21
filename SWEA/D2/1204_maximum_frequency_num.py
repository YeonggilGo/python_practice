T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    scores = list(map(int, input().split()))

    fre = [0] * 101

    for score in scores:
        fre[score] += 1

    fre.reverse()
    ans = 100 - fre.index(max(fre))

    print(f'#{tc} {ans}')
