# 주사위 게임
# 1부터 6까지 숫자가 적힌 주사위가 두 개 있습니다. 두 주사위를 굴렸을 때 나온 숫자를 각각 a, b라고 했을 때 얻는 점수는 다음과 같습니다.


# - a와 b가 모두 홀수라면 a2 + b2 점을 얻습니다.
# - a와 b 중 하나만 홀수라면 2 × (a + b) 점을 얻습니다.
# - a와 b 모두 홀수가 아니라면 |a - b| 점을 얻습니다.
# 두 정수 a와 b가 매개변수로 주어질 때, 얻는 점수를 return 하는 solution 함수를 작성해 주세요.
def solution(a: int, b: int):
    if a % 2 == 1 and b % 2 == 1:
        return (a**2) + (b**2)
    elif b % 2 == 1 or a % 2 == 1:
        return 2 * (a + b)
    else:
        return abs(a - b)


def another_solution(a: int, b: int):
    if a % 2 and b % 2:
        return a * a + b * b
    elif a % 2 or b % 2:
        return 2 * (a + b)
    return abs(a - b)


print(solution(3, 5))
print(solution(6, 1))
print(solution(2, 4))
