def rob_linear(nums):
    prev1 = 0
    prev2 = 0

    for money in nums:
        current = max(prev1, prev2 + money)
        prev2 = prev1
        prev1 = current

    return prev1


def house_robber(nums):

    if len(nums) == 1:
        return nums[0]

    return max(
        rob_linear(nums[:-1]),
        rob_linear(nums[1:])
    )


def main():
    nums = [2, 3, 2]

    print("Houses:", nums)
    print("Maximum Money:", house_robber(nums))


if __name__ == "__main__":
    main()