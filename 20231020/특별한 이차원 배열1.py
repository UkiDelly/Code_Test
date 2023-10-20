# 특별한 이차원 배열1

# 정수 n이 매개변수로 주어질 때, 다음과 같은 n × n 크기의 이차원 배열 arr를 return 하는 solution 함수를 작성해 주세요.
# arr[i][j] (0 ≤ i, j < n)의 값은 i = j라면 1, 아니라면 0입니다.


def solution(n: int):
    answer = [[0] * n for i in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j:
                answer[i][j] = 1
    return answer


print(solution(3))


def another_solution(n: int):
    answer = [[0] * n for i in range(n)]
    for i in range(n):
        answer[i][i] = 1
    return answer


print(another_solution(3))
