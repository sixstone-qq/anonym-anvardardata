#!/usr/bin/env python3
from unittest import TestCase
from sumdiv import sum_div


class TestSumDiv(TestCase):
    def test_10(self):
        self.assertEqual(sum_div(10), [1, 2, 3, 4])

    def test_5(self):
        self.assertEqual(sum_div(5), [1, 4])

    def test_6(self):
        self.assertEqual(sum_div(6), [1, 2, 3])

    def test_1(self):
        self.assertEqual(sum_div(1), [1])

    def test_20(self):
        self.assertEqual(sum_div(20), [1, 2, 3, 14])

    def test_200(self):
        self.assertEqual(sum_div(200),
                         [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
                          11, 12, 13, 14, 15, 16, 17, 18, 29])
