# 문제 설명
# 길이가 같은 두 문자열 str1과 str2가 주어집니다.
#
# 두 문자열의 각 문자가 앞에서부터 서로 번갈아가면서 한 번씩 등장하는 문자열을 만들어 return 하는 solution 함수를 완성해 주세요.


#  입출력의 예
# 	str1	str2	result
# "aaaaa"	"bbbbb"	"ababababab"


# 내 답변
def solution(str1, str2) -> str:
    list_1 = list(str1)
    list_2 = list(str2)
    list_3 = []

    for i in range(len(str1)):
        list_3.append(list_1[i])
        list_3.append(list_2[i])
    return "".join(list_3)


# 배울게 있는 답변
def another_solution(str1: str, str2: str) -> str:
    answer: str = ""
    # zip은 2개의 list을 모아 각각 원소 값을 tuple 형식으로 반환한다.
    for i, j in zip(str1, str2):
        answer += i + j
    return answer


fisrtString: str = "ababababab"
secondString: str = "cdcdcdcdcd"
print(solution(fisrtString, secondString))
print(another_solution(fisrtString, secondString))
