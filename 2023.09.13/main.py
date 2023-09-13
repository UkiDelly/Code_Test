def solution(my_string: str):
    answer = []
    while len(my_string) > 0:
        answer.append(my_string)
        my_string = my_string[1:]
    return sorted(answer)
print(solution("banana"))