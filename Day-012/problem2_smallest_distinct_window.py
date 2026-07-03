def smallest_distinct_window(s):

    distinct = len(set(s))

    frequency = {}

    left = 0
    count = 0
    minimum = float("inf")

    for right in range(len(s)):

        frequency[s[right]] = frequency.get(s[right], 0) + 1

        if frequency[s[right]] == 1:
            count += 1

        while count == distinct:

            minimum = min(minimum, right - left + 1)

            frequency[s[left]] -= 1

            if frequency[s[left]] == 0:
                count -= 1

            left += 1

    return minimum


def main():

    s = "abcda"

    print("String:", s)
    print("Smallest Window Length:", smallest_distinct_window(s))


if __name__ == "__main__":
    main()