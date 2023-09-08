# 등차수열의 특정한 항만 더하기
# 두 정수 a, d와 길이가 n인 boolean 배열 included가 주어집니다. 첫째항이 a, 공차가 d인 등차수열에서 included[i]가 i + 1항을 의미할 때,
# 이 등차수열의 1항부터 n항까지 included가 true인 항들만 더한 값을 return 하는 solution 함수를 작성해 주세요.


# 내 답변
def solution(a: int, d: int, included: list[bool]) -> int:
    answer: int = 0
    num_list: list[int] = [a]
    for _ in range(len(included) - 1):
        num_list.append(num_list[-1] + d)

    for num, con in zip(num_list, included):
        if con:
            answer += num
    return answer


# 다른 답변
def another_solution(a: int, d: int, included: list[bool]) -> int:
    # included의 값(f)가 true 인 경우 a에가다 ()
    return sum(a + i * d for i, f in enumerate(included) if f)


print(another_solution(3, 4, [True, False, False, True, True]))
