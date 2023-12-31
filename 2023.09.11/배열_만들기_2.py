# 배열 만들기 2
# 정수 l과 r이 주어졌을 때, l 이상 r이하의 정수 중에서 숫자 "0"과 "5"로만 이루어진 모든 정수를 오름차순으로 저장한 배열을 return 하는 solution 함수를 완성해 주세요.

# 만약 그러한 정수가 없다면, -1이 담긴 배열을 return 합니다.


# 내 힘으로 풀지 못함...
def solution(l: int, r: int) -> list[int]:
    answer = []
    for i in range(l, r + 1):
        if all(num in ["0", "5"] for num in str(i)):
            answer.append(i)
    if len(answer) == 0:
        return [-1]
    return answer


def another_solution(l: int, r: int) -> list[int]:
    answer = []
    for i in range(l, r + 1):
        if set(str(i)).issubset({"0", "5"}):
            answer.append(i)
    if len(answer) == 0:
        return [-1]
    return answer


print(solution(5, 555))
print(another_solution(5, 555))
