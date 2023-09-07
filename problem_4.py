# 연산 ⊕는 두 정수에 대한 연산으로 두 정수를 붙여서 쓴 값을 반환합니다. 예를 들면 다음과 같습니다.

# 12 ⊕ 3 = 123
# 3 ⊕ 12 = 312
# 양의 정수 a와 b가 주어졌을 때, a ⊕ b와 b ⊕ a 중 더 큰 값을 return 하는 solution 함수를 완성해 주세요.

# 단, a ⊕ b와 b ⊕ a가 같다면 a ⊕ b를 return 합니다.


# 내 방법
def solution(a: int, b: int) -> int:
    first: int = int(str(a) + str(b))
    second: int = int(str(b) + str(a))

    print(f"first: {first}")
    print(f"second: {second}")

    return first if first > second or first == second else second

    # if first > second or first == second:
    #     return first
    # else:
    #     return second


# 이상적인 방법
def another_solution(a: int, b: int) -> int:
    stringA, stringB = str(a), str(b)
    return max(int(stringA + stringB), int(stringB + stringA))


fistNum: int = 12
secondNum: int = 9
print(solution(fistNum, secondNum))
print(another_solution(fistNum, secondNum))
