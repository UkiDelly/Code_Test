# 모든 대문자는 소문자로 변경해야한다.
# 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외하고 모두 삭제
# 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환합니다.
# 마침표가(.)가 처음이나 끝에 위치한다면 제거
# 빈 문자열이면 aa를 대입
# 문자열이 15자 이상이면 16자부터 자르기
# 2자 이하라면 마지막 인덱스를 문자열의*3의 길이가 될때까지 반복


def solution(newId: str) -> str:
    # 모든 대문자를 소문자로 변경
    newId = newId.lower()

    # 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외하고 모두 삭제
    for i in newId:
        if not i.isalnum() and i not in "-_.":
            newId = newId.replace(i, "")

    # 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환합니다.
    while ".." in newId:
        newId = newId.replace("..", ".")

    # 마침표가 (.)가 처음이나 끝에 위치한다면 제거
    newId = newId.strip(".")

    # 빈 문자열이면 a를 대입
    newId = "a" if len(newId) == 0 else newId

    # 문자열이 15자 이상이면 16자부터 자르기
    newId = newId[:15]

    # 2자 이하라면 마지막 인덱스를 문자열의*3의 길이가 될때까지 반복
    if len(newId) < 3:
        newId += newId[-1] * (3 - len(newId))

    # 마침표가 (.)가 처음이나 끝에 위치한다면 제거
    newId = newId.strip(".")

    return newId


solution("...!@BaT#*..y.abcdefghijklm")

# # 문제 1. 문자열의 마지막 문자를 2번더 붙이기
# prob: str = "jun"
# print(prob + (prob[-1] * 2))

# # 문제 2. 대문자는 소문자로 치환하는 코드 작성
# prob2 = "Jun"
# print(prob2.lower())

# # 문제 3. a,b,c,d,e 숫자 그리고 언더스코어(_)나 대쉬(-)를 모두 제거하려는
# table = str.maketrans("", "", "1234567890abcde-_")
# s = "hello_world123"
# print(s.translate(table))

import re


def regex_solution(newId: str) -> str:
    newId = newId.lower()
    newId = re.sub("[^a-z0-9-_.]", "", newId)
    newId = re.sub("[.]{2,}", ".", newId)
    newId = re.sub("^[.]|[.]$", "", newId)
    newId = "a" if len(newId) == 0 else newId
    newId = newId[:15]
    if len(newId) < 3:
        newId += newId[-1] * (3 - len(newId))
    newId = re.sub("^[.]|[.]$", "", newId)
    return newId
