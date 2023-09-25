def solution(a: int, b: int, n: int):
    answer = 0
    bottles = n
    while bottles >= a:
        b_new, b_left = divmod(bottles, a)
        b_new *= b
        answer += b_new
        bottles = b_new + b_left
    return answer


print(solution(3, 1, 20))