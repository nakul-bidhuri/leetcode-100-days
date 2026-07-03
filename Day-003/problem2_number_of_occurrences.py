def count_occurrences(arr, target):
    count = 0

    for num in arr:
        if num == target:
            count += 1

    return count


def main():
    arr = [1, 1, 2, 2, 2, 2, 3]
    target = 2

    result = count_occurrences(arr, target)

    print("Array:", arr)
    print("Target:", target)
    print("Occurrences:", result)


if __name__ == "__main__":
    main()