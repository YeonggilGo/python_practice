import heapq

for tc in range(1, int(input()) + 1):
    N, A = map(int, input().split())
    numbers = [A]
    ans = 0
    cnt = 1
    for i in range(1, N + 1):
        cnt += 2
        a, b = map(int, input().split())
        heapq.heappush(numbers, b)
        heapq.heappush(numbers, a)
        ans += min(numbers[cnt//2],numbers[cnt//2+1]) % 20171109
    print(f'#{tc} {ans}')