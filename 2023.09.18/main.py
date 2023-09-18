def solution(n: int, m: int, section: list[int]):
    count = 1

    # section의 첫번째 요소를 시작점으로 지정
    # section[0] 부터 n의  section[0] + m 부분까지는 1번으로 칠하는게 가능하다.
    # 예) section=[2,3,6] , n = 8, m = 4일때,
    #  section[0]인 n의 2번째 구역부터 5번째 구역까지는 1번으로 칠할수 있다.
    #  그러므로 section의 값중, section[i] - paint >= m
    paint = section[0]
    for i in range(len(section)):
        if section[i] - paint >= m:
            count += 1
            paint = section[i]
    return count


print(solution(4, 1, [1, 2, 3, 4]))
# print(solution(8, 4, [2, 3, 6]))
