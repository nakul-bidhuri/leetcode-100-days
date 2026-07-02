def remove_element(nums, val):
    k = 0

    for num in nums:
        if num != val:
            nums[k] = num
            k += 1

    return k


def main():
    nums = [3, 2, 2, 3]
    val = 3

    k = remove_element(nums, val)

    print("Remaining Count:", k)
    print("Remaining Array:", nums[:k])


if __name__ == "__main__":
    main()