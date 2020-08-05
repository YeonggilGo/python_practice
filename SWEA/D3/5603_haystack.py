T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    haystacks = []
    for i in range(N):
        haystacks.append(int(input()))
    aver = sum(haystacks) // N

    ans = 0

    for haystack in haystacks:
        ans += abs(aver - haystack)

    print(f'#{tc} {ans//2}')
