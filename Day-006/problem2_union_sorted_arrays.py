def union_arrays(a, b):
    i = j = 0
    result = []

    def add(x):
        if not result or result[-1] != x:
            result.append(x)

    while i < len(a) and j < len(b):
        ai, bj = a[i], b[j]
        if ai < bj:
            add(ai)
            i += 1
        elif ai > bj:
            add(bj)
            j += 1
        else:
            add(ai)
            i += 1
            j += 1

    while i < len(a):
        add(a[i])
        i += 1

    while j < len(b):
        add(b[j])
        j += 1

    return result


def main():

    a = [1, 2, 3, 4, 5]
    b = [1, 2, 3, 6, 7]

    print("Union:", union_arrays(a, b))


if __name__ == "__main__":
    main()