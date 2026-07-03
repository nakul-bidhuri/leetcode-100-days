def transpose_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    transpose = []

    for col in range(cols):
        new_row = []

        for row in range(rows):
            new_row.append(matrix[row][col])

        transpose.append(new_row)

    return transpose


def main():
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    result = transpose_matrix(matrix)

    print("Original Matrix:")
    for row in matrix:
        print(row)

    print("\nTranspose Matrix:")
    for row in result:
        print(row)


if __name__ == "__main__":
    main()