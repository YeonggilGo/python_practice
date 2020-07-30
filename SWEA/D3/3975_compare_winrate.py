from fractions import Fraction

ans = []
T = int(input())
for tc in range(1, T + 1):
    a, b, c, d = map(int, input().split())
    alice = Fraction(f'{a}/{b}')
    bob = Fraction(f'{c}/{d}')

    if alice > bob:
        ans.append('ALICE')
    elif alice < bob:
        ans.append('BOB')
    else:
        ans.append('DRAW')

for tc in range(T):
    print(f'#{tc+1} {ans[tc]}')
