for tc in range(1, 11):
    N = int(input())
    boxes = list(map(int, input().split()))
    height = [0] * 101

    for i in range(len(boxes)):
        height[boxes[i]] += 1

    min_ = 0
    max_ = 100

    while height[min_] == 0:
        min_ += 1
    while height[max_] == 0:
        max_ -= 1

    for i in range(N):
        height[min_] -= 1
        height[min_ + 1] += 1

        height[max_] -= 1
        height[max_ - 1] += 1

        while height[max_] == 0:
            max_ -= 1
        while height[min_] == 0:
            min_ += 1

    print(f'#{tc} {max_-min_}')
