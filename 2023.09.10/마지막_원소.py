# 마지막 두 원소
# 정수 리스트 num_list가 주어질 때, 마지막 원소가 그전 원소보다 크면 마지막 원소에서 그전 원소를 뺀 값을,
# 마지막 원소가 그전 원소보다 크지 않다면 마지막 원소를 두 배한 값을 추가하여 return하도록 solution 함수를 완성해주세요.


# 내 대답
def solution(num_list: list[int]) -> list[int]:
    two_last_index: list[int] = num_list[-2:]

    if two_last_index[0] > two_last_index[1]:
        num_list.append(two_last_index.pop() * 2)
        return num_list
    else:
        num_list.append(two_last_index[1] - two_last_index[0])
        return num_list


# 이상적인 대답
def another_solution(num_list: list[int]) -> list[int]:
    n1, n2 = num_list[-2], num_list[-1]
    if n1 >= n2:
        num_list.append(n2 * 2)
    else:
        num_list.append(n1 - n2)
    return num_list


print(solution([5, 2, 1, 7, 5]))
print(another_solution([5, 2, 1, 7, 5]))
