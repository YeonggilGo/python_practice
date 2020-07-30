T = int(input())


def padovan(n):
    if len(memo) < n:
        if n not in [1, 2, 3]:
            while len(memo) < n:
                memo.append(memo[-2]+memo[-3])
    return memo[n-1]


for tc in range(1, T + 1):
    memo = [1, 1, 1]
    print(f'#{tc} {padovan(int(input()))}')
