def is_isomorphic(s, t):

    if len(s) != len(t):
        return False

    map_st = {}
    map_ts = {}

    for i in range(len(s)):

        if s[i] in map_st:
            if map_st[s[i]] != t[i]:
                return False
        else:
            map_st[s[i]] = t[i]

        if t[i] in map_ts:
            if map_ts[t[i]] != s[i]:
                return False
        else:
            map_ts[t[i]] = s[i]

    return True


def main():

    s = "egg"
    t = "add"

    print("String 1:", s)
    print("String 2:", t)
    print("Isomorphic:", is_isomorphic(s, t))


if __name__ == "__main__":
    main()