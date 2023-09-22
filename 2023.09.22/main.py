def solution(myString: str, pat: str):
    result = ""

    index = 0
    while pat not in myString[index : index + 1]:
        result += myString[index]
        index += 1

    return result


print(solution("AbCdEFG", "dE"))
