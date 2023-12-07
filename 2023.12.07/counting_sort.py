def solution(arr: list[int]):
    answer = [0 for _ in range(100)]

    for i in arr:
        answer[i] += 1

    return answer


print(solution([1, 1, 3, 2, 1]))
