def solution(words, queries):
    answer = [0] * len(queries)
    for word in words:
        for idx, querie in enumerate(queries):
            if len(word) == len(querie):
                same = 1
                for i in range(len(word)):
                    if querie[i] != '?' and word[i] != querie[i]:
                        same = 0
                        break
                answer[idx] += same
    return answer