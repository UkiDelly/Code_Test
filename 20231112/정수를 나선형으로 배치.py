#  정수를 나선형으로 배치하기

# 양의 정수 n이 매개변수로 주어집니다. n × n 배열에 1부터 n2 까지 정수를 인덱스 [0][0]부터 시계방향 나선형으로 배치한 이차원 배열을 return 하는 solution 함수를 작성해 주세요.


def solution(n: int):
    snake = [n]
    answer = [[0] * n for _ in range(n)]
    d = (0, 1), (1, 0), (0, -1), (-1, 0)
    count, x, y = 0, -1, 0

    while n > 1:
        n -= 1
        snake.append(n)
        snake.append(n)

    for i in range(len(snake)):
        for _ in range(snake[i]):
            y += d[i % 4][0]
            x += d[i % 4][1]
            count += 1
            answer[y][x] = count

    return answer


print(solution(4))


l = [
    [1, 2, 3, 4],
    [12, 13, 14, 5],
    [11, 16, 15, 6],
    [10, 9, 8, 7],
]

ll = [
    [1, 2, 3, 4, 5],
    [16, 17, 18, 19, 6],
    [15, 24, 25, 20, 7],
    [14, 23, 22, 21, 8],
    [13, 12, 11, 10, 9],
]
