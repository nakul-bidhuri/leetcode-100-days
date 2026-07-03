def plus_one(digits):
    n = len(digits)

    for i in range(n - 1, -1, -1):

        if digits[i] < 9:
            digits[i] += 1
            return digits

        digits[i] = 0

    return [1] + digits


def main():
    digits = [1, 2, 3]

    result = plus_one(digits)

    print("Original Number:", digits)
    print("After Plus One:", result)


if __name__ == "__main__":
    main()