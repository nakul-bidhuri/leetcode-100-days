def card_game(cards):

    left = 0
    right = len(cards) - 1

    player1 = 0
    player2 = 0

    turn = 0

    while left <= right:

        if cards[left] > cards[right]:
            picked = cards[left]
            left += 1
        else:
            picked = cards[right]
            right -= 1

        if turn == 0:
            player1 += picked
            turn = 1
        else:
            player2 += picked
            turn = 0

    return player1, player2


def main():

    cards = [4, 1, 2, 10]

    p1, p2 = card_game(cards)

    print("Player 1 Score:", p1)
    print("Player 2 Score:", p2)


if __name__ == "__main__":
    main()