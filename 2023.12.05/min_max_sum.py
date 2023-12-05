# 내코드
def miniMaxSum(arr: list[int]):
    # Write your code here
    answer_list = []
    for i in arr:
        result = sum(arr) - i
        answer_list.append(result)
    print(f"{min(answer_list)} {max(answer_list)}")


# 이상적인 코드
def solution(arr: list[int]):
    # arr의 합에서 제일 작은 수를 제외할때 가장 큰 숫자가 되고,
    # arr의 합에서 제일 큰 수를 제외할때 가장 작은 숫자가 된다.
    print(sum(arr) - min(arr), sum(arr) - max(arr))


miniMaxSum([1, 2, 3, 4, 5])
