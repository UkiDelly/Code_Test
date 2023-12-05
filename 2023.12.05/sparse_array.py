def matchingStrings(strings: list[str], queries: list[str]) -> list[int]:
    answer = []
    for q in queries:
        answer.append(strings.count(q))
    return answer


print(matchingStrings(["ab", "ab", "abc"], ["ab", "abc", "bc"]))
