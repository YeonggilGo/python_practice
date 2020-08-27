if __name__ == '__main__':
    for tc in range(1, int(input()) + 1):
        s = input()
        stack = []
        brackets_dict = {'}': '{', ')': '('}
        flag = 1
        for letter in s:
            if letter in brackets_dict.values():
                stack.append(letter)
            if letter in brackets_dict.keys():
                if not stack or brackets_dict[letter] != stack[-1]:
                    flag = 0
                    break
                else:
                    stack.pop()
        if stack:
            flag = 0

        print('#{} {}'.format(tc, flag))