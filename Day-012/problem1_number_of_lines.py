def number_of_lines(widths, s):

    lines = 1
    current_width = 0

    for ch in s:

        width = widths[ord(ch) - ord('a')]

        if current_width + width <= 100:
            current_width += width
        else:
            lines += 1
            current_width = width

    return [lines, current_width]


def main():

    widths = [10] * 26
    s = "abcdefghijklmnopqrstuvwxyz"

    result = number_of_lines(widths, s)

    print("Output:", result)


if __name__ == "__main__":
    main()