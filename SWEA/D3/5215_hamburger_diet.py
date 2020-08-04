from math import gcd


def my_gcd(numbers):
    tmp = gcd(numbers[0], numbers[1])
    for i in range(2, len(numbers)):
        tmp = gcd(tmp, numbers[i])
    return tmp


T = int(input())
for tc in range(1, T + 1):
    N, L = map(int, input().split())
    ingredients = []
    for _ in range(N):
        ingredients.append(list(map(int, input().split())))
    ingredients.sort(key=lambda x: x[1])
    g = my_gcd([ing[1] for ing in ingredients])

    dp = [[0 if i == 0 or j == 0 else 1 for i in range(L//g + 1)] for j in range(N + 1)]

    for j in range(1, N + 1):
        for i in range(1, L//g + 1):
            if ingredients[j - 1][1] <= i*g:
                dp[j][i] = max(dp[j - 1][i], ingredients[j - 1][0] + dp[j - 1][i - ingredients[j - 1][1]//g])
            else:
                dp[j][i] = dp[j - 1][i]

    print(f'#{tc} {dp[-1][-1]}')
