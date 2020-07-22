# Answer
def all_list_sum(list_):
    res = 0
    for i in range(len(list_)):
        for j in range(len(list_[i])):
            res += list_[i][j]
    return res


print(all_list_sum([[1], [2, 3], [4, 5, 6], [7, 8, 9, 10]]))
