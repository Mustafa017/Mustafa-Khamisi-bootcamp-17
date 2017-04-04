from unittest import TestCase
from prime_numbers import prime_num

class TestPrime_num(TestCase):
    def test_prime_num(self):
        self.assertEquals(prime_num(10),[2,3,5,7])
