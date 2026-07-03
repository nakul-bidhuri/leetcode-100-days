def check_equal_arrays(a, b):

    if len(a) != len(b):
        return False

    frequency = {}

    for num in a:
        frequency[num] = frequency.get(num, 0) + 1

    for num in b:

        if num not in frequency:
            return False

        frequency[num] -= 1

        if frequency[num] < 0:
            return False

    return True


def main():

    a = [1, 2, 5, 4, 0]
    b = [2, 4, 5, 0, 1]

    result = check_equal_arrays(a, b)

    print("Array A:", a)
    print("Array B:", b)
    print("Are Equal:", result)


if __name__ == "__main__":
    main()