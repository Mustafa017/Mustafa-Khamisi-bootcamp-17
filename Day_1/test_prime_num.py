from unittest import TestCase
from prime_numbers import prime_num


class TestPrime_num(TestCase):
    def test_correct_output(self):
        self.assertEqual(prime_num(15), [2, 3, 5, 7,11,13], msg="Return the correct output")

    def test_upto_num(self):
        self.assertEqual(prime_num(13), [2, 3, 5, 7,11,13], msg="The result should include n, the argument of the function")

    def test_negative_num(self):
        self.assertEqual(prime_num(-1), "invalid input", msg="Return invalid input if argument is negative number")

    def test_less_than2(self):
        self.assertEqual(prime_num(1), "0 and 1 are not prime", msg="there exists no prime numbers below 2")

    def test_even_num(self):
        self.assertEquals(prime_num(10), [2,3,5,7], msg="All even numbers except 2 are not prime numbers")
