import unittest
from solution import Solution


class TestSortList(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_empty_nums(self):
        self.assertEqual(self.solution.sortList([]), [])

    def test_mixed_nums(self):
        self.assertEqual(self.solution.sortList([1, -1, 0, 2]), [-1, 0, 1, 2])

    def test_positive_nums(self):
        self.assertEqual(self.solution.sortList([2, 7, 3, 1]), [1, 2, 3, 7])

    def test_negative_nums(self):
        self.assertEqual(self.solution.sortList([-2, -1, -3, -5]), [-5, -3, -2, -1])