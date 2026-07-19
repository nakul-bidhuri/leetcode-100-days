def process(text):

    stack = []

    for ch in text:

        if ch == "#":

            if stack:
                stack.pop()

        else:
            stack.append(ch)

    return "".join(stack)


def backspace_compare(s, t):

    return process(s) == process(t)


def main():

    s = "ab#c"
    t = "ad#c"

    print("Are Equal:", backspace_compare(s, t))


if __name__ == "__main__":
    main()