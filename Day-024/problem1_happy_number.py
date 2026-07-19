def next_number(n):

    total = 0

    while n > 0:

        digit = n % 10
        total += digit * digit
        n //= 10

    return total


def is_happy(n):

    seen = set()

    while n != 1 and n not in seen:

        seen.add(n)

        n = next_number(n)

    return n == 1


def main():

    n = 19

    print("Happy Number:", is_happy(n))


if __name__ == "__main__":
    main()