def sorted_squares(nums):

    n = len(nums)

    result = [0] * n

    left = 0
    right = n - 1
    index = n - 1

    while left <= right:

        if abs(nums[left]) > abs(nums[right]):

            result[index] = nums[left] * nums[left]
            left += 1

        else:

            result[index] = nums[right] * nums[right]
            right -= 1

        index -= 1

    return result


def main():

    nums = [-4, -1, 0, 3, 10]

    print("Sorted Squares:", sorted_squares(nums))


if __name__ == "__main__":
    main()