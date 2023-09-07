# 조건 문자열
# 문제 설명
# 문자열에 따라 다음과 같이 두 수의 크기를 비교하려고 합니다.

# 두 수가 n과 m이라면
# ">", "=" : n >= m
# "<", "=" : n <= m
# ">", "!" : n > m
# "<", "!" : n < m
# 두 문자열 ineq와 eq가 주어집니다. ineq는 "<"와 ">"중 하나고, eq는 "="와 "!"중 하나입니다. 그리고 두 정수 n과 m이 주어질 때, n과 m이 ineq와 eq의 조건에 맞으면 1을 아니면 0을 return하도록 solution 함수를 완성해주세요.

# 제한 사항
# 1 ≤ n, m ≤ 100
# 입출력 예
# ineq	eq	n	m	result
# "<"	"="	20	50	1
# ">"	"!"	41	78	0
# 입출력 예 설명
# 입출력 예 #1

# 20 <= 50은 참이기 때문에 1을 return합니다.
# 입출력 예 #2

# 41 > 78은 거짓이기 때문에 0을 return합니다.


# 내 답변
def solution(ineq: str, eq: str, n: int, m: int) -> int:
    template: dict[str, int] = {
        "<": n <= m,
        ">": n >= m,
        "=": n >= m or n <= m,
        "!": n != m,
    }
    print(template[ineq])
    print(template[eq])
    return int(template[ineq] and template[eq])


# 다른 답변
def another_solution(ineq: str, eq: str, n: int, m: int) -> int:
    # eval()함수를 사용해서 값을 구한다
    # eval()함수는 문자열로 식을 입력 받아 실행한다.
    return int(eval(f"{n} {ineq}{eq}  {m}".replace("!", "")))


print(another_solution("<", "=", 20, 50))
