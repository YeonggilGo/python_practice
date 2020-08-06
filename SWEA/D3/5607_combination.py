# 페르마의 소정리
# p가 소수이고 a가 p로 나누어지지 않는 정수이면 다음과 같은 특징을 가진다.
# a^p ≡ a (mod p)
# a^p-1 ≡ 1 (mod p)
# a^p-2 ≡ a^-1 (mod p)

# 거듭제곱의 분할정복
# a^n 을 구할때 다음과 같이 구할 수 있다.
# IF n%2==0, a^n = a^(n/2) * a^(n/2) = ...
# IF n%2!=0, a^n = a * a^(n/2) * a^(n/2) = ...

# 분할 정복을 이용한 pow + MOD
# O(log x)
def power(N, x):
    if x == 0:
        return 1
    else:
        if x % 2:
            tmp = power(N, (x - 1) / 2)
            return tmp * (tmp % MOD) * N % MOD
        else:
            tmp = power(N, x / 2)
            return tmp * (tmp % MOD)


facto = [1]
MOD = 1234567891
T = int(input())
for tc in range(1, T + 1):
    N, R = map(int, input().split())
    idx = len(facto)
    while idx < N + 1:
        facto.append((facto[-1] * idx) % MOD)
        idx += 1
    top = facto[N] % MOD
    bottom = (power(facto[R], MOD - 2) * power(facto[N - R], MOD - 2)) % MOD
    res = (top * bottom) % MOD
    print(f'#{tc} {res}')
