def first_occurrence(haystack, needle):

    n = len(haystack)
    m = len(needle)

    for i in range(n - m + 1):

        if haystack[i:i + m] == needle:
            return i

    return -1


def main():

    haystack = "sadbutsad"
    needle = "sad"

    result = first_occurrence(haystack, needle)

    print("Haystack:", haystack)
    print("Needle:", needle)
    print("First Occurrence Index:", result)


if __name__ == "__main__":
    main()