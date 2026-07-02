def missing_number(nums):
    n = len(nums)

    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)

    return expected_sum - actual_sum


def main():
    nums = [3, 0, 1]

    result = missing_number(nums)

    print("Array:", nums)
    print("Missing Number:", result)


if __name__ == "__main__":
    main()