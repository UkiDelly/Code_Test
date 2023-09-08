# 이어 붙인 수

# 정수가 담긴 리스트 num_list가 주어집니다. num_list의 홀수만 순서대로 이어 붙인 수와 짝수만 순서대로 이어 붙인 수의 합을 return하도록
# solution 함수를 완성해주세요.


# 내 대답
def solution(num_list: list[int]) -> int:
    odd_list: str = ""
    even_list: str = ""

    for num in num_list:
        if num % 2 == 0:
            even_list += str(num)
        else:
            odd_list += str(num)

    return eval(f"{odd_list} + {even_list}")


print(solution([3, 4, 5, 2, 1]))
