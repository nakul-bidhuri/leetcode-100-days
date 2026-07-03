import re


def most_common_word(paragraph, banned):

    banned = {word.lower() for word in banned}

    words = re.findall(r"[a-zA-Z]+", paragraph.lower())

    frequency = {}

    answer = ""
    maximum = 0

    for word in words:

        if word not in banned:

            frequency[word] = frequency.get(word, 0) + 1

            if frequency[word] > maximum:
                maximum = frequency[word]
                answer = word

    return answer


def main():

    paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
    banned = ["hit"]

    print("Most Common Word:", most_common_word(paragraph, banned))


if __name__ == "__main__":
    main()