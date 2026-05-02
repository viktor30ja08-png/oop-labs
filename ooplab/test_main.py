import unittest
from main import validate_matrix, multiply_matrix_by_scalar, get_sum_of_min_in_columns


class TestMatrixOperations(unittest.TestCase):

    def setUp(self):
        # Дані для тестування
        self.matrix_b = [
            [1, -5,   8,  12],
            [4,  2, -10,   3],
            [-7,  9,   0, -15]
        ]
        self.scalar_a = 3

    def test_multiply_matrix_by_scalar(self):
        """Перевіряємо, чи правильно матриця множиться на число"""
        expected_result = [
            [3, -15,  24,  36],
            [12,  6, -30,   9],
            [-21, 27,   0, -45]
        ]
        result = multiply_matrix_by_scalar(self.matrix_b, self.scalar_a)
        self.assertEqual(result, expected_result)

    def test_get_sum_of_min_in_columns(self):
        """Перевіряємо, чи правильно рахується сума найменших елементів стовпців"""
        matrix_c = multiply_matrix_by_scalar(self.matrix_b, self.scalar_a)
        result = get_sum_of_min_in_columns(matrix_c)
        self.assertEqual(result, -111)

    def test_empty_matrix_validation(self):
        """Перевіряємо, чи спрацьовує помилка при порожній матриці"""
        with self.assertRaises(ValueError):
            validate_matrix([])

    def test_invalid_shape_matrix(self):
        """Перевіряємо, чи спрацьовує помилка при нерівних рядках матриці"""
        invalid_matrix = [
            [1, 2, 3],
            [4, 5]
        ]
        with self.assertRaises(ValueError):
            validate_matrix(invalid_matrix)


if __name__ == '__main__':
    unittest.main()
