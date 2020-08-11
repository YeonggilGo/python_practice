for tc in range(1, 11):
    N = int(input())
    numbers = list(input())
    idx = 0
    while '(' in numbers:
        new_numbers = []
        while idx < len(numbers):
            if numbers[idx] != '(':
                new_numbers.append(numbers[idx])
            else:

    print(f'#{tc} {ans}')
