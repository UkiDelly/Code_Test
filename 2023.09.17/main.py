def solution(arr: list[int]):
    try:
        first = arr.index(2)
        # end = arr[::-1].index(2) + 1
        end = 0
        for i in range(len(arr)):
            if arr[i] == 2:
                end = i
        return arr[first : end + 1]
        # return arr[first : (-end) + 1]

    except ValueError:
        return [-1]


print(solution([1, 2, 1, 4, 5, 2, 9]))
print(solution([1, 2, 1]))
print(solution([1, 1, 1]))
print(solution([1, 2, 1, 2, 1, 10, 2, 1]))
