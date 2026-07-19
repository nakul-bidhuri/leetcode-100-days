def triplet_sum_exists(arr):

    arr.sort()

    n = len(arr)

    for k in range(n - 1, -1, -1):

        left = 0
        right = k - 1

        while left < right:

            total = arr[left] + arr[right]

            if total == arr[k]:
                return True

            elif total < arr[k]:
                left += 1

            else:
                right -= 1

    return False


def main():

    arr = [4, 1, 3, 2, 5]

    print("Triplet Exists:", triplet_sum_exists(arr))


if __name__ == "__main__":
    main()