def array_sum(arr):
    total = 0

    for num in arr:
        total += num

    return total


def main():
    arr = [12, 35, 1, 10, 34, 1]

    result = array_sum(arr)

    print("Array:", arr)
    print("Sum:", result)


if __name__ == "__main__":
    main()