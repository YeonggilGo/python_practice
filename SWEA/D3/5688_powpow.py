from fractions import Fraction
from math import isclose

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    res = pow(N, Fraction(1 / 3))
    if not isclose(res, round(res)):
        res = -1
    print(f'#{tc} {round(res)}')