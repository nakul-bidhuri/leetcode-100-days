def determine_gender(username):

    unique_characters = set(username)

    if len(unique_characters) % 2 == 0:
        return "CHAT WITH HER!"
    else:
        return "IGNORE HIM!"


def main():

    username = "alex"

    print("Username:", username)
    print(determine_gender(username))


if __name__ == "__main__":
    main()