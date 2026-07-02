def find_largest(arr):
    largest = arr[0]

    for num in arr:
        if num > largest:
            largest = num

    return largest


def main():
    arr = [12, 35, 1, 10, 34, 1]

    print("Array:", arr)
    print("Largest Element:", find_largest(arr))


if __name__ == "__main__":
    main()