def find_content_children(g, s):

    g.sort()
    s.sort()

    child = 0
    cookie = 0

    while child < len(g) and cookie < len(s):

        if s[cookie] >= g[child]:
            child += 1

        cookie += 1

    return child


def main():

    g = [1, 2, 3]
    s = [1, 1]

    print("Satisfied Children:", find_content_children(g, s))


if __name__ == "__main__":
    main()