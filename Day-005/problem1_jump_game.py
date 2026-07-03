def can_jump(nums):
    max_reach = 0

    for i in range(len(nums)):

        if i > max_reach:
            return False

        max_reach = max(max_reach, i + nums[i])

    return True


def main():
    nums = [2, 3, 1, 1, 4]

    result = can_jump(nums)

    print("Array:", nums)
    print("Can Reach Last Index:", result)


if __name__ == "__main__":
    main()