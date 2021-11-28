import unittest
from solution import Solution


class TestMergeTwoSortedLists(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_empty_lists(self):
        self.assertEqual(self.solution.mergeTwoLists([], []), [])

    def test_one_empty_list(self):
        self.assertEqual(self.solution.mergeTwoLists([], [5]), [5])

    def test_two_mixed_lists(self):
        self.assertEqual(self.solution.mergeTwoLists([1, 4], [-6, 2, 3]), [-6, 1, 2, 3, 4])

    def test_positive_lists(self):
        self.assertEqual(self.solution.mergeTwoLists([5], [4, 8, 13]), [4, 5, 8, 13])

    def test_negative_lists(self):
        self.assertEqual(self.solution.mergeTwoLists([-5], [-10, -5, -2]), [-10, -5, -5, -2])