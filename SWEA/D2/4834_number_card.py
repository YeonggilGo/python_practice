T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    card = input()
    numbers = [0] * 10
    for number in card:
        numbers[int(number)] += 1

    max_ = sorted([(i, n) for i, n in enumerate(numbers) if n == max(numbers)], reverse=True)[0]

    print('#', tc, sep='', end=' ')
    print(max_[0], max_[1], sep=' ')
