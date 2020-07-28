import math

# Eratosthenes' sieve
# 0.56s

numbers = [True] * 1000001
numbers[0], numbers[1] = False, False
numbers = []
for i in range(2, 1000001):
    if numbers[i]:
        print(i, end=' ')
    for j in range(i, 1000001, i):
        numbers[j] = False


# 각각 계산 하는 방식
# 1.8s
# 체가 훨씬 더 빠르다.


def is_prime(n):
    for i in range(2, math.floor(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True


for i in range(2, 1000001):
    if is_prime(i):
        print(i, end=' ')
