from collections import deque


def is_palindrome(s):
    s = deque(s)
    for i in range(len(s) // 2):
        front = s.popleft()
        end = s.pop()
        if front == '?' or end == '?':
            continue
        elif front != end:
            return False
    return True


T = int(input())

for tc in range(1, T + 1):
    ans = 'Exist ' if is_palindrome(input()) else 'Not exist'
    print(f'#{tc} {ans}')
