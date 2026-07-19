def pair_with_target(arr, target):

    left = 0
    right = len(arr) - 1

    while left < right:

        total = arr[left] + arr[right]

        if total == target:
            return True

        elif total < target:
            left += 1

        else:
            right -= 1

    return False


def main():

    arr = [1, 2, 4, 6, 10]
    target = 8

    print("Pair Exists:", pair_with_target(arr, target))


if __name__ == "__main__":
    main()