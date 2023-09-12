# 주사위 게임 3
# 1부터 6까지 숫자가 적힌 주사위가 네 개 있습니다. 네 주사위를 굴렸을 때 나온 숫자에 따라 다음과 같은 점수를 얻습니다.

# 네 주사위에서 나온 숫자가 모두 p로 같다면 1111 × p점을 얻습니다.
# 세 주사위에서 나온 숫자가 p로 같고 나머지 다른 주사위에서 나온 숫자가 q(p ≠ q)라면 (10 × p + q)2 점을 얻습니다.
# 주사위가 두 개씩 같은 값이 나오고, 나온 숫자를 각각 p, q(p ≠ q)라고 한다면 (p + q) × |p - q|점을 얻습니다.
# 어느 두 주사위에서 나온 숫자가 p로 같고 나머지 두 주사위에서 나온 숫자가 각각 p와 다른 q, r(q ≠ r)이라면 q × r점을 얻습니다.
# 네 주사위에 적힌 숫자가 모두 다르다면 나온 숫자 중 가장 작은 숫자 만큼의 점수를 얻습니다.
# 네 주사위를 굴렸을 때 나온 숫자가 정수 매개변수 a, b, c, d로 주어질 때, 얻는 점수를 return 하는 solution 함수를 작성해 주세요.


# 내 대답
def solution(a: int, b: int, c: int, d: int) -> int | None:
    num_set: set[int] = set([a, b, c, d])
    num_list: list[int] = sorted([a, b, c, d])

    # 두 숫자가 같고(p) 나머지 두숫자가 다를때(q,r)면 (q*r)
    def two_are_same(num_list: list[int]) -> int:
        p = max(num_list, key=num_list.count)
        q, r = filter(lambda x: x != p, num_list)
        return q * r

    # 세 숫자(p)가 같고 다른 숫자(q)라면 (10 * p + q) ** 2
    def three_are_same(num_list: list[int]) -> int:
        p = max(num_list, key=num_list.count)
        q = min(num_list, key=num_list.count)
        return (10 * p + q) ** 2

    # 두 숫자가 같고(p) 나머지 두숫자가 다를때(q,r)면 (q*r)
    # [1,1,3,4]
    # [1,3,3,4]
    # [1,2,3,3]
    if len(num_set) == 3:
        return two_are_same(num_list)

    # 모든 숫자(p)가 같으면 1111*p
    if len(num_set) == 1:
        return 1111 * a

    # 두숫자가 같고(p) 나머지 두 숫자도 같으면(q) (p+q) * abs(p-q)
    if len(set(num_list[:2])) == 1 and len(set(num_list[2:])) == 1:
        p = num_list[0]
        q = num_list[-1]
        return (p + q) * abs(p - q)

    # 세 숫자(p)가 같고 다른 숫자(q)라면 (10 * p + q) ** 2
    # [1,3,3,3]
    # [1,1,1,3]
    if len(num_set) == 2:
        return three_are_same(num_list)

    # 모든 숫자가 다르면 min(a,b,c,d)
    if len(num_set) == 4:
        return min(a, b, c, d)


print(solution(2, 2, 2, 2))
print(solution(4, 1, 4, 4))
print(solution(6, 3, 3, 6))
print(solution(2, 5, 2, 6))
print(solution(6, 4, 2, 5))

print("=================================================")


from collections import Counter


def another_solution(a: int, b: int, c: int, d: int) -> int | None:
    counter: Counter[int] = Counter([a, b, c, d])
    num_list: list[int] = sorted([a, b, c, d])
    num_set: set[int] = set([a, b, c, d])

    # 두 숫자가 같고(p) 나머지 두숫자가 다를때(q,r)면 (q*r)
    if len(counter.most_common()) == 3:
        p = counter.most_common(1)[0][0]
        q, r = filter(lambda x: x != p, num_list)
        return q * r

    # 모든 숫자(p)가 같으면 1111*p
    if len(num_set) == 1:
        return 1111 * a

    # 두숫자가 같고(p) 나머지 두 숫자도 같으면(q) (p+q) * abs(p-q)
    if counter.most_common(1)[0][1] == 2:
        p = num_list[0]
        q = num_list[-1]
        return (p + q) * abs(p - q)

    # 세 숫자(p)가 같고 다른 숫자(q)라면 (10 * p + q) ** 2
    if counter.most_common(1)[0][1] == 3:
        p = counter.most_common()[0][0]
        q = counter.most_common()[-1][0]
        return (10 * p + q) ** 2

    # 모든 숫자가 다르면 min(a,b,c,d)
    if len(num_set) == 4:
        return min(num_set)


print(another_solution(2, 2, 2, 2))
print(another_solution(4, 1, 4, 4))
print(another_solution(6, 3, 3, 6))
print(another_solution(2, 5, 2, 6))
print(another_solution(6, 4, 2, 5))
