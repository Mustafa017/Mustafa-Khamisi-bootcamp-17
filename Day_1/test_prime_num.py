from unittest import TestCase
from prime_numbers import prime_num


class TestPrime_num(TestCase):
    def test_prime_num(self):
        self.assertEquals(prime_num(10), [2, 3, 5, 7])


class TestPrime_num(TestCase):
    def test_prime_num(self):
        self.assertEquals(prime_num(-1), "invalid input")


class TestPrime_num(TestCase):
    def test_prime_num(self):
        self.assertEquals(prime_num(1), "0 and 1 are not prime")


class TestPrime_num(TestCase):
    def test_prime_num(self):
        self.assertEquals(prime_num(24), None)
