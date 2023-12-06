def solution(n: int):
    # 정수를 이진수로 변환하고, 비트의 개수를 32비트로 맞춥니다.
    binary = bin(n & 0xFFFFFFFF)[2:].zfill(32)
    # 비트를 뒤집습니다.
    flipped_binary = "".join("1" if bit == "0" else "0" for bit in binary)
    # 뒤집은 비트를 다시 정수로 변환합니다.
    flipped_num = int(flipped_binary, 2)
    return flipped_num


print("solution 1:", solution(3))
print("solution 1:", solution(2147483647))
print("solution 1:", solution(1))
print("solution 1:", solution(0))


def another_solution(n: int):
    return ~n & 0xFFFFFFFF


print("solution 2:", another_solution(3))
print("solution 2:", another_solution(2147483647))
print("solution 2:", another_solution(1))
print("solution 2:", another_solution(0))
