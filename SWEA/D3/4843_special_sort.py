import sys

sys.stdin = open('특별한 정렬.txt', 'r')
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    numbers = list(map(int,input().split()))
    for i in range(10):
        if i%2:
            min_idx = i
            for j in range(i+1,N):
                if numbers[j] < numbers[min_idx]:
                    min_idx = j
            numbers[i], numbers[min_idx] = numbers[min_idx], numbers[i]
        else:
            max_idx = i
            for j in range(i+1,N):
                if numbers[j] > numbers[max_idx]:
                    max_idx = j
            numbers[i], numbers[max_idx] = numbers[max_idx], numbers[i]
    ans = ' '.join(map(str,numbers[:10]))
    print('#{} {}'.format(tc,ans))