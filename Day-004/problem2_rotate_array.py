def rotate_array(nums, k):
    n = len(nums)

    k = k % n

    return nums[-k:] + nums[:-k]


def main():
    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 3

    result = rotate_array(nums, k)

    print("Original Array:", nums)
    print("Rotated Array :", result)


if __name__ == "__main__":
    main()