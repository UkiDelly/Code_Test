# 수 조작하기 1
# 정수 n과 문자열 control이 주어집니다. control은 "w", "a", "s", "d"의 4개의 문자로 이루어져 있으며, control의 앞에서부터 순서대로 문자에 따라 n의 값을 바꿉니다.


# "w" : n이 1 커집니다.
# "s" : n이 1 작아집니다.
# "d" : n이 10 커집니다.
# "a" : n이 10 작아집니다.
# 위 규칙에 따라 n을 바꿨을 때 가장 마지막에 나오는 n의 값을 return 하는 solution 함수를 완성해 주세요.
def solution(n: int, control: str) -> int:
    for c in control:
        if c == "w":
            n += 1
        elif c == "s":
            n -= 1
        elif c == "d":
            n += 10
        elif c == "a":
            n -= 10
    return n


# 이상적인 대답
def another_solution(n: int, control: str) -> int:
    # zip은 2개의 list을 모아 각각 원소 값을 tuple 형식으로 반환한다.
    # 즉 key에는 { "w" : 1, "s" : -1, "d" : 10 , "a" : -10 } 가 들어오는 것이다.
    key: dict[str, int] = dict(zip(["w", "s", "d", "a"], [1, -1, 10, -10]))

    # control을 for문 돌려서 key[키 이릅(w,s,a,d)]의 값(1,-1,10,-10)의 합을 계산한다.
    return n + sum(key[c] for c in control)


print(solution(0, "wsdawsdassw"))
