def solution(arr: list[int], idx: int):
    tmp_list = arr[idx:]

    try:
        index = tmp_list.index(1)
        return idx + index
    except ValueError:
        return -1


print(solution([0, 0, 0, 1], 1))
