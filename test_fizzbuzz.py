# -*- coding: utf-8 -*-
import fizzbuzz
import unittest


class TestFizzBuzz(unittest.TestCase):
    def test_three(self):
        self.assertEqual(fizzbuzz.process(6), 'Fizz')

    def test_five(self):
        self.assertEqual(fizzbuzz.process(10), 'Buzz')

    def test_three_and_five(self):
        self.assertEqual(fizzbuzz.process(15), 'FizzBuzz')

    def test_regular(self):
        self.assertEqual(fizzbuzz.process(2), 2)
        self.assertEqual(fizzbuzz.process(11), 11)
