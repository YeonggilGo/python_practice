from collections import deque

for _ in range(10):
    N = int(input())
    pwd = input().split()
    com_len = input()
    coms = deque(input().split())
    while coms:
        now = coms.popleft()
        if now == 'I':
            pos = int(coms.popleft())
            n = int(coms.popleft())
            for i in range(n):
                pwd.insert(pos + i, coms.popleft())
        elif now == 'D':
            pos = int(coms.popleft())
            n = int(coms.popleft())
            for i in range(n):
                pwd.pop(pos)

    ans = ' '.join(pwd[:10])

    print(f'#{_+1} {ans}')
