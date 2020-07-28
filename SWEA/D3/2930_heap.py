T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    coms = []
    for i in range(N):
        coms.append(list(map(int, input().split())))

    heap = []

    print(f'#{tc}', end=' ')
    for com in coms:
        # 삽입 과정
        if com[0] == 1:
            heap.append(com[1])
            idx = len(heap) - 1
            while heap[idx] > heap[idx // 2]:
                heap[idx], heap[idx // 2] = heap[idx // 2], heap[idx]
                idx //= 2
        else:
            print(heap[0], end=' ')
            if heap:
                heap[0] = heap.pop()
                idx = 0
                while heap[idx] < max(heap[idx * 2], heap[idx * 2 + 1]):
                    large = idx * 2 if heap[idx *
                                            2] > heap[idx * 2 + 1] else idx * 2 + 1
                    heap[large], heap[idx] = heap[idx], heap[large]
            else:
                print(-1, end=' ')
