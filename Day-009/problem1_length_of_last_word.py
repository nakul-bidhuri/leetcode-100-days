def length_of_last_word(s):

    s = s.strip()

    count = 0

    for i in range(len(s) - 1, -1, -1):

        if s[i] == " ":
            break

        count += 1

    return count


def main():

    s = "Hello World"

    print("Input :", s)
    print("Length of Last Word :", length_of_last_word(s))


if __name__ == "__main__":
    main()