def swap1(a, b):
    if a > b:
        b, a = a, b
    return a, b


def swap1_helper(a, b):
    print("method one swap")
    print("original: ", a, b)
    a, b = swap1(a, b)
    print("after: ", a, b)
    print()


def swap2(a, b):
    if a > b:
        swap = a
        a = b
        b = swap
    return a, b


def swap2_helper(a, b):
    print("method two swap")
    print("original ", a, b)
    a, b = swap2(a, b)
    print("after: ", a, b)
    print()


def test_swappers():
    swap1_helper(11, 1)
    swap1_helper(41, 33)
    swap2_helper(11, 1)
    swap2_helper(41, 33)


if __name__ == "__main__":
    test_swappers()

