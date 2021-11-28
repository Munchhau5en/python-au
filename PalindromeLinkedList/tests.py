import unittest
from solution import Solution


class TestSolution(unittest.TestCase):
    def test_palindrome(self):
        self.assertEqual(self.solution.isPalindrome([1, 2, 1]), True)
    def test_non_palindrome(self):
        self.assertEqual(self.solution.isPalindrome([1, 2, 3, 1]), False)

    def test_empty_list(self):
        self.assertEqual(self.solution.isPalindrome([]), True)

    def test_one_element(self):
        self.assertEqual(self.solution.isPalindrome([1]), True)
