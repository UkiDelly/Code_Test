from collections import Counter


def solution(a: list[int]):
    counter = Counter(a)
    most_common = counter.most_common()
    return most_common[-1][0]


print(solution([1, 2, 3, 4, 3, 2, 1]))
