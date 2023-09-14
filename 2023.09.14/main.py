def solution(my_string: str, m: int, c: int):
    tmp = []
    while len(my_string) > 1:
        tmp.append(my_string[:m])
        my_string = my_string[m:]

    answer = "".join(i[c - 1] for i in tmp)
    return answer


print(solution("ihrhbakrfpndopljhygc", 4, 2))
