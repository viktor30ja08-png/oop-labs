def validate_matrix(matrix):

    if not matrix or not matrix[0]:
        raise ValueError("Матриця порожня або не ініціалізована.")

    cols_count = len(matrix[0])
    for row in matrix:
        if len(row) != cols_count:
            raise ValueError(
                "Матриця має бути правильною прямокутною (рядки різної довжини не допускаються).")


def multiply_matrix_by_scalar(matrix, scalar):

    validate_matrix(matrix)
    rows = len(matrix)
    cols = len(matrix[0])

    matrix_c = []
    for i in range(rows):
        new_row = []
        for j in range(cols):
            new_row.append(scalar * matrix[i][j])
        matrix_c.append(new_row)

    return matrix_c


def get_sum_of_min_in_columns(matrix):

    validate_matrix(matrix)
    rows = len(matrix)
    cols = len(matrix[0])

    sum_of_min_elements = 0

    for j in range(cols):
        min_in_col = matrix[0][j]
        for i in range(1, rows):
            if matrix[i][j] < min_in_col:
                min_in_col = matrix[i][j]
        sum_of_min_elements += min_in_col

    return sum_of_min_elements


def print_matrix(matrix):

    for row in matrix:
        print(" ".join(f"{val:5d}" for val in row))


def main():
    try:
        scalar_a = 3
        matrix_b = [
            [1, -5,   8,  12],
            [4,  2, -10,   3],
            [-7,  9,   0, -15]
        ]

        print("Початкова матриця B:")
        print_matrix(matrix_b)
        print(f"Константа a = {scalar_a}\n")

        matrix_c = multiply_matrix_by_scalar(matrix_b, scalar_a)
        print("Результуюча матриця C = a * B:")
        print_matrix(matrix_c)
        print()

        sum_min = get_sum_of_min_in_columns(matrix_c)
        print(f"Сума найменших елементів кожного стовпця матриці C: {sum_min}")

    except Exception as e:
        print(f"Помилка: {e}")


if __name__ == "__main__":
    main()
