def solution(arr: list[int], k: int):
    answer = []
    for i in arr:
        if i not in answer:
            answer.append(i)
        else:
            continue
    l = len(answer)

    if l < k:
        answer.extend([-1] * (k - l))
        return answer
    else:
        return answer[:k]


print(solution([0, 1, 1, 1, 1], 4))
