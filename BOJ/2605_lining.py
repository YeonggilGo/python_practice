N = int(input())
ticket = list(map(int, input().split()))
order = []
for i in range(1, N + 1):
    order.insert(i - 1 - ticket[i - 1], i)
print(*order)
