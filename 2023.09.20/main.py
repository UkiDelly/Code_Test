def solution(myString: str, pat: str):
    return int(pat.lower() in myString.lower())


print(solution("AbCdEfG", "aBc"))
