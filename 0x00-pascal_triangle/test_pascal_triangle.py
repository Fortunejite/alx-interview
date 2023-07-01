import unittest
pascal_triangle = __import__('0-pascal_triangle').pascal_triangle

class PascalTriangleTest(unittest.TestCase):
    def test_pascal_triangle(self):
        # Test case: Generate Pascal's triangle with 5 rows
        expected_result = [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
        self.assertEqual(pascal_triangle(5), expected_result)

        # Test case: Generate Pascal's triangle with 1 row
        expected_result = [[1]]
        self.assertEqual(pascal_triangle(1), expected_result)

        # Test case: Generate Pascal's triangle with 0 rows
        expected_result = []
        self.assertEqual(pascal_triangle(0), expected_result)

        # Test case: Generate Pascal's triangle with 10 rows
        expected_result = [
            [1],
            [1, 1],
            [1, 2, 1],
            [1, 3, 3, 1],
            [1, 4, 6, 4, 1],
            [1, 5, 10, 10, 5, 1],
            [1, 6, 15, 20, 15, 6, 1],
            [1, 7, 21, 35, 35, 21, 7, 1],
            [1, 8, 28, 56, 70, 56, 28, 8, 1],
            [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
        ]
        self.assertEqual(pascal_triangle(10), expected_result)

if __name__ == '__main__':
    unittest.main()
