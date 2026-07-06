def move_zeroes(nums):

    left = 0

    for right in range(len(nums)):

        if nums[right] != 0:

            nums[left], nums[right] = nums[right], nums[left]

            left += 1

    return nums


def main():

    nums = [0, 1, 0, 3, 12]

    print("Original Array:", nums)

    move_zeroes(nums)

    print("After Moving Zeroes:", nums)


if __name__ == "__main__":
    main()