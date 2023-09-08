# 원소들의 곱과 합
# 정수가 담긴 리스트 num_list가 주어질 때, 모든 원소들의 곱이 모든 원소들의 합의 제곱보다 작으면 1을 크면 0을 return하도록 solution 함수를 완성해주세요.

# 내 코드
from functools import reduce


def solution(num_list: list[int]) -> int:
    return 1 if sum(num_list) ** 2 > reduce(lambda x, y: x * y, num_list) else 0


print(solution([1, 2, 3, 4, 5]))
