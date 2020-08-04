primes = []
numbers = [True] * 1000001
numbers[0], numbers[1] = False, False
for i in range(2, 1000001):
    if numbers[i]:
        primes.append(i)
    for j in range(i, 1000001, i):
        numbers[j] = False

T = int(input())
for tc in range(1, T + 1):
    D, A, B = map(int, input().split())
    ans = 0
    for prime in primes:
        if prime < A:
            continue
        elif prime > B:
            break
        if str(D) in str(prime):
            ans += 1

    print(f'#{tc} {ans}')
