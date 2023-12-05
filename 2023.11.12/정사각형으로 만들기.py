# 정사각형으로 만들기


def solution(arr: list[list[int]]):
    arr_len = len(arr)
    if arr_len > len(arr[0]):
        for inner_arr in arr:
            while len(inner_arr) != arr_len:
                inner_arr.append(0)
    elif arr_len < len(arr[0]):
        inner_arr_len = len(arr[0])
        l = [0] * inner_arr_len
        for _ in range(inner_arr_len - arr_len):
            arr.append(l)
    return arr


print(solution([[57, 192, 534, 2], [9, 345, 192, 999]]))
