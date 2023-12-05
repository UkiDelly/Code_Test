# 날짜 비교하기
# 정수 배열 date1과 date2가 주어집니다. 두 배열은 각각 날짜를 나타내며 [year, month, day] 꼴로 주어집니다. 각 배열에서 year는 연도를, month는 월을, day는 날짜를 나타냅니다.

# 만약 date1이 date2보다 앞서는 날짜라면 1을, 아니면 0을 return 하는 solution 함수를 완성해 주세요.


from datetime import datetime


def solution(date1: list[int], date2: list[int]):
    d1, d2 = datetime(*date1), datetime(*date2)
    return int(date1 < date2)


def another_solution(date1: list[int], date2: list[int]):
    return int(date1 < date2)


print(solution([2021, 12, 28], [2021, 12, 29]))
print(solution([1024, 10, 24], [1024, 10, 24]))
print(another_solution([2021, 12, 28], [2021, 12, 29]))
print(another_solution([1024, 10, 24], [1024, 10, 24]))
