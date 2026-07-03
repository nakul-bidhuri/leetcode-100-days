def distinct_subsequences(s):

    n = len(s)

    dp = [0] * (n + 1)

    dp[0] = 1

    last = {}

    for i in range(1, n + 1):

        dp[i] = 2 * dp[i - 1]

        ch = s[i - 1]

        if ch in last:
            dp[i] -= dp[last[ch] - 1]

        last[ch] = i

    return dp[n]


def better_string(s1, s2):

    if distinct_subsequences(s1) >= distinct_subsequences(s2):
        return s1

    return s2


def main():

    s1 = "abc"
    s2 = "aac"

    print("Better String:", better_string(s1, s2))


if __name__ == "__main__":
    main()