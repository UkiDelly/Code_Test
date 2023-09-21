# 다른 대답
def solution(s: str):
    position = {}
    answer = []
    for index, char in enumerate(s):
        index += 1

        if char not in position:
            answer.append(-1)
        else:
            prev_index = position[char]
            answer.append(index - prev_index)
        position[char] = index
    return answer


print(solution("banana"))
