# 크기가 작은 문자열

# 숫자로 이루어진 문자열 t와 p가 주어질 때, t에서 p와 길이가 같은 부분문자열 중에서, 이 부분문자열이 나타내는 수가 p가 나타내는 수보다 작거나 같은 것이 나오는 횟수를 return하는 함수 solution을 완성하세요.

# 예를 들어, t="3141592"이고 p="271" 인 경우, t의 길이가 3인 부분 문자열은 314, 141, 415, 159, 592입니다. 이 문자열이 나타내는 수 중 271보다 작거나 같은 수는 141, 159 2개 입니다.


def solution(t: str, p: str):
    p_len = len(p)
    str_list = [t[int(x) : int(x) + p_len] for x in range(len(t))]
    str_list = list(filter(lambda x: len(x) == p_len, str_list))
    print(str_list)
    count = 0
    for item in str_list:
        if int(item) <= int(p):
            count += 1
    return count


print(solution("3141592", "271"))
