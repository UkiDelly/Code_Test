def solution(arr: list[list[int]]):
    size: int = len(arr)
    left_to_right: int = 0
    right_to_left: int = 0

    for i in range(size):
        left_to_right += arr[i][i]
        right_to_left += arr[i][(size - 1) - i]

    return abs(left_to_right - right_to_left)


print(solution([[11, 2, 4], [4, 5, 6], [10, 8, -12]]))
