def process_string(s):

    vowels = "aeiouAEIOU"

    result = ""

    for ch in s:

        if ch not in vowels:
            result += "." + ch.lower()

    return result


def main():

    s = "Programming"

    print("Original String :", s)
    print("Processed String:", process_string(s))


if __name__ == "__main__":
    main()