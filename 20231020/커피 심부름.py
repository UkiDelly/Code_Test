# 커피 심부름

# 팀의 막내인 철수는 아메리카노와 카페 라테만 판매하는 카페에서 팀원들의 커피를 사려고 합니다.
# 아메리카노와 카페 라테의 가격은 차가운 것과 뜨거운 것 상관없이 각각 4500, 5000원입니다.
# 각 팀원에게 마실 메뉴를 적어달라고 하였고,
# 그 중에서 메뉴만 적은 팀원의 것은 차가운 것으로 통일하고
# "아무거나"를 적은 팀원의 것은 차가운 아메리카노로 통일하기로 하였습니다.

# 각 직원이 적은 메뉴가 문자열 배열 order로 주어질 때,
# 카페에서 결제하게 될 금액을 return 하는 solution 함수를 작성해주세요.
# order의 원소는 아래의 것들만 들어오고, 각각의 의미는 다음과 같습니다.
import re


def solution(order: list[str]):
    # 아무거나는 아이스 아메리카노로 통일
    # 아메리카노는 4500원
    # 카페라테는 5000원
    menu = {"americano": 4500, "cafelatte": 5000, "anything": 4500}
    answer = 0
    pattern = re.compile(r"(ice|hot)")
    for i in order:
        i = pattern.sub("", i)
        if i in menu:
            answer += menu[i]
    return answer


print(solution(["cafelatte", "americanoice", "hotcafelatte", "anything"]))


def another_solution(order: list[str]):
    answer = 0
    for i in order:
        # cafelatte를 제외하고는 모두 4500원이므로 먼저 4500원일 더함
        answer += 4500

        # order에 latte라는 단어가 존재하면, 500원을 추가 즉, latte라는 단어가 존재하면 5000원을 더하는것과 같음.
        if "latte" in i:
            answer += 500
    return answer


print(another_solution(["cafelatte", "americanoice", "hotcafelatte", "anything"]))
