def solution(numbers: list[int], n: int):
    sum = 0
    for number in numbers:
        sum += number
        if sum > n:
            return sum


print(solution([58, 44, 27, 10, 100], 139))