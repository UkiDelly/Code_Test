# 특별한 이차원 배열 2

# n × n 크기의 이차원 배열 arr이 매개변수로 주어질 때, arr이 다음을 만족하면 1을
# 아니라면 0을 return 하는 solution 함수를 작성해 주세요.


def solution(arr: list[list[int]]):
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] != arr[j][i]:
                return 0
    return 1


def another_solution(arr: list[list[int]]):
    return int(arr == list(map(list, zip(*arr))))


print(solution([[5, 192, 33], [192, 72, 95], [33, 95, 999]]))
print(
    solution(
        [
            [19, 498, 258, 587],
            [63, 93, 7, 754],
            [258, 7, 1000, 723],
            [587, 754, 723, 81],
        ]
    )
)
