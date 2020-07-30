# heap을 혼자 구현해보려고 혼자 뻘짓을 했는데
# 시간초과가 난다. heap sort방식을 쓰지 않으면 시간이
# 오래 걸리나 보다. 그냥 heapq 모듈을 사용하자. 일단은

# from collections import deque
# T = int(input())

# for tc in range(1, T + 1):
#     N = int(input())

#     print(f'#{tc}', end=' ')
#     heap = deque()

#     for _ in range(N):
#         com = list(map(int, input().split()))
#         # 삽입 과정
#         if com[0] == 1:
#             heap.append(com[1])
#             idx = len(heap) - 1
#             while heap[idx] > heap[(idx-1) // 2]:
#                 heap[idx], heap[(idx-1) // 2] = heap[(idx-1) // 2], heap[idx]
#                 idx = (idx - 1) // 2
#                 if idx == 0:
#                     break
#         else:
#             if heap:
#                 print(heap.popleft(), end=' ')
#                 if not heap:
#                     continue

#                 heap.appendleft(heap.pop())
#                 idx = 0
#                 while True:
#                     if len(heap) > (idx+1) * 2:
#                         tar_idx = (idx+1) * \
#                             2 if heap[(idx+1) * 2] > heap[(idx+1) *
#                                                           2 - 1] else (idx+1) * 2 - 1
#                     elif len(heap) > (idx + 1) * 2 - 1:
#                         tar_idx = (idx + 1) * 2 - 1
#                     else:
#                         break
#                     if heap[idx] > heap[tar_idx]:
#                         break
#                     else:
#                         heap[tar_idx], heap[idx] = heap[idx], heap[tar_idx]
#                         idx = tar_idx
#             else:
#                 print(-1, end=' ')

#     print()

# 왠지 모르겠는데 모듈을 써도 시간초과다. 뭔가가 더 필요하다.

# import heapq

import heapq
T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    heap = []
    print(f'#{tc}', end=' ')
    for _ in range(N):
        com = list(map(int, input().split()))
        if com[0] == 1:
            heap.append(com[1])
        else:
            if heap:
                tmp = heapq.heappop(heap)
                print(tmp, end=' ')
            else:
                print(-1, end=' ')
    print()

# python에서 제공하는 heapq 모듈은 최소힙만을 제공하므로 최대힙으로 튜플을 사용하면 시간이 더걸려서 시간초과가 나는게 아닐까?라는 생각을 바탕으로
# heapq를 사용해 최대힙을 다시 만들어서 해보자

# 해보니까 좀더 빠르긴하다. 그래도 부족하다


class ReverseLessThan(object):
    def __init__(self, value):
        self.value = value

    def __lt__(self, other):
        return self.value > other.value

    def __repr__(self):
        return str(self.value)


def heappush(heap, item):
    reverse_item = ReverseLessThan(item)
    heapq.heappush(heap, reverse_item)


def heappop(heap):
    reverse_item = heapq.heappop(heap)
    return reverse_item.value


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    heap = []]
    print(f'#{tc}', end=' ')
    for _ in range(N):
        com = list(map(int, input().split()))
        if com[0] == 1:
            heappush(heap, com[1])
        else:
            if heap:
                print(heap.heappop(heap), end=' ')
            else:
                print(-1, end=' ')
    print()
