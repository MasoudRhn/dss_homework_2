import unittest
from math_quiz import Random_int, Random_operator, Operation


class TestMathGame(unittest.TestCase):

    def test_random_int(self):

        min_val = 1
        max_val = 10
        for _ in range(1000):
            rand_num = Random_int(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_random_operator(self):

        for _ in range(1000):
            operator = Random_operator()
            self.assertIn(
                operator, ["+", "-", "*"], "Operator should be one of ['+', '-', '*']"
            )

    def test_operation(self):

        test_cases = [
            (5, 2, "+", "5 + 2", 7),
            (10, 3, "-", "10 - 3", 7),
            (4, 3, "*", "4 * 3", 12),
        ]

        for num1, num2, operator, expected_problem, expected_answer in test_cases:
            problem, answer = Operation(num1, num2, operator)
            self.assertEqual(
                problem,
                expected_problem,
                f"Expected problem '{expected_problem}' but got '{problem}'",
            )
            self.assertEqual(
                answer,
                expected_answer,
                f"Expected answer '{expected_answer}' but got '{answer}'",
            )


if __name__ == "__main__":
    unittest.main()
