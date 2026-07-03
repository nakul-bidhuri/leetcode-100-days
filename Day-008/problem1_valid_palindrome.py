def is_palindrome(s):

    cleaned = ""

    for ch in s:
        if ch.isalnum():
            cleaned += ch.lower()

    left = 0
    right = len(cleaned) - 1

    while left < right:

        if cleaned[left] != cleaned[right]:
            return False

        left += 1
        right -= 1

    return True


def main():

    s = "A man, a plan, a canal: Panama"

    print("Input:", s)
    print("Palindrome:", is_palindrome(s))


if __name__ == "__main__":
    main()