if __name__ == '__main__':
    for tc in range(1, int(input()) + 1):
        s = input()
        stack = []
        for letter in s:
            if stack and letter == stack[-1]:
                stack.pop()
            else:
                stack.append(letter)
        print('#{} {}'.format(tc, len(stack)))