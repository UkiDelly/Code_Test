# 주사위 게임

# 1부터 6까지 숫자가 적힌 주사위가 세 개 있습니다. 세 주사위를 굴렸을 때 나온 숫자를 각각 a, b, c라고 했을 때 얻는 점수는 다음과 같습니다.

# 세 숫자가 모두 다르다면 a + b + c 점을 얻습니다.
# 세 숫자 중 어느 두 숫자는 같고 나머지 다른 숫자는 다르다면 (a + b + c) × (a2 + b2 + c2 )점을 얻습니다.
# 세 숫자가 모두 같다면 (a + b + c) × (a2 + b2 + c2 ) × (a3 + b3 + c3 )점을 얻습니다.
# 세 정수 a, b, c가 매개변수로 주어질 때, 얻는 점수를 return 하는 solution 함수를 작성해 주세요.


# 내 대답
def solution(a: int, b: int, c: int) -> int:
    if a == b == c:
        return (a + b + c) * (a**2 + b**2 + c**2) * (a**3 + b**3 + c**3)
    elif a == b or a == c or b == c:
        return (a + b + c) * (a**2 + b**2 + c**2)
    else:
        return a + b + c


# 다른 답변
def another_solution(a: int, b: int, c: int) -> int:
    # a, b, c를 set로 변환한 다음 길이를 구한다 (set는 중복된 값이 존재할수 없기 때문에 )
    check: int = len(set([a, b, c]))

    # 모두가 같은 값이라 길이가 1인 경우
    if check == 1:
        # ( a + a + a ) * ( a**2 + a**2 + a**2 ) * ( a**3 + a**3 + a**3 )
        # 모두가 같은 값이기 때문에 a,b,c 아무거나 골라서 사용해도 상관 없다
        return (a * 3) * (3 * (a**2)) * (3 * (a**3))
    elif check == 2:
        return (a + b + c) * (a**2 + b**2 + c**2)
    else:
        return a + b + c


print(another_solution(5, 3, 3))
