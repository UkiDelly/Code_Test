#  이차원 배열 대각선 순회하기


def solution(board: list[list[int]], k: int):
    answer = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if i + j <= k:
                answer += board[i][j]
    return answer


print(solution([[0, 1, 2], [1, 2, 3], [2, 3, 4], [3, 4, 5]], 2))
