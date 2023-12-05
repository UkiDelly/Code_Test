# 조건에 맞는 수열 반환하기 3
# 정수 배열 arr와 자연수 k가 주어집니다.

# 만약 k가 홀수라면 arr의 모든 원소에 k를 곱하고, k가 짝수라면 arr의 모든 원소에 k를 더합니다.

# 이러한 변환을 마친 후의 arr를 return 하는 solution 함수를 완성해 주세요.


def solution(arr: list[int], k: int):
    answer = []

    # for num in arr:
    #     if k % 2:
    #         answer.append(num * k)
    #     else:
    #         answer.append(num + k)
    # return answer

    return [num * k if k % 2 else num + k for num in arr]


print(solution([1, 2, 3, 100, 99, 98], 3))
