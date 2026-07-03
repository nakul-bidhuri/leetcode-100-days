def remove_spaces(s):

    result = ""

    for ch in s:

        if ch != " ":
            result += ch

    return result


def main():

    s = "C od ing"

    print("Original String :", s)
    print("Without Spaces :", remove_spaces(s))


if __name__ == "__main__":
    main()