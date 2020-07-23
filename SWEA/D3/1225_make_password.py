from collections import deque
for _ in range(10):
    t = int(input())
    num = deque(map(int, input().split()))

    c = 1
    while (True):
        tmp = num.popleft()
        tmp = tmp - c if tmp > c else 0
        num.append(tmp)

        if not tmp:
            break
        c = c + 1 if c != 5 else 1

    num = ' '.join(list(map(str, num)))

    print(f'#{t} {num}')
