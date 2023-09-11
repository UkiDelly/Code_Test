#  카운트 업
# 정수 start_num와 end_num가 주어질 때, start_num부터 end_num까지의 숫자를 차례로 담은 리스트를 return하도록 solution 함수를 완성해주세요.


# 내 대답
def solution(start_num: int, end_num: int) -> list[int]:
    return [x for x in range(start_num, end_num + 1)]


# 다른 대답
def another_solution(start_num: int, end_num: int) -> list[int]:
    return list(range(start_num, end_num + 1))


print(solution(3, 10))
