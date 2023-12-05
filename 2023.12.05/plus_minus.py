def plusMinus(arr: list[int]):
    # Write your code here
    total = len(arr)
    p, n, z = (
        len(list(filter(lambda x: x > 0, arr))),
        len(list(filter(lambda x: x < 0, arr))),
        len(list(filter(lambda x: x == 0, arr))),
    )

    print(f"{(p/total):.6f}")
    print(f"{(n/total):.6f}")
    print(f"{(z/total):.6f}")


plusMinus([-4, 3, -9, 0, 4, 1])
