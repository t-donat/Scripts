import unittest
import time
from primes import prime_numbers_v1, prime_numbers_v2, prime_numbers_v3


class TestPrimeCalculators(unittest.TestCase):

    def setUp(self) -> None:
        super(TestPrimeCalculators, self).setUp()

        bool_prime_1_to_10 = [False, True, True, False, True, False, True, False, False, False]
        bool_prime_11_to_20 = [True, False, True, False, False, False, True, False, True, False]
        bool_prime_21_to_30 = [False, False, True, False, False, False, False, False, True, False]

        self.prime_booleans = bool_prime_1_to_10 + bool_prime_11_to_20 + bool_prime_21_to_30

    def tearDown(self) -> None:
        super(TestPrimeCalculators, self).tearDown()

        # this sleep times is included in order to guarantee that the print statements are fully executed before the
        # test suite is torn down

        time.sleep(0.005)

    @property
    def prime_booleans(self):
        return self._prime_booleans

    @prime_booleans.setter
    def prime_booleans(self, new_booleans):
        if not isinstance(new_booleans, list):
            error = type(new_booleans)
            raise TypeError(f"List of prime booleans: Expected type list, got {error} instead!")

        if any(not isinstance(item, bool) for item in new_booleans):
            raise TypeError("The reference list of prime numbers contains elements that aren't booleans!")
        self._prime_booleans = new_booleans

    def test_v1_correct(self):
        """ Assert the correctness of the v1 prime number calculation algorithm using the list of prime booleans"""

        for index, expected_result in enumerate(self.prime_booleans):

            n = index + 1
            self.assertEqual(prime_numbers_v1(n), expected_result)

    def test_v2_correct(self):
        """ Assert the correctness of the v2 prime number calculation algorithm using the list of prime booleans"""

        for index, expected_result in enumerate(self.prime_booleans):

            n = index + 1
            self.assertEqual(prime_numbers_v2(n), expected_result)

    def test_v3_correct(self):
        """ Assert the correctness of the v3 prime number calculation algorithm using the list of prime booleans"""

        for index, expected_result in enumerate(self.prime_booleans):
            n = index + 1
            self.assertEqual(prime_numbers_v3(n), expected_result)

    def test_v1_runtime(self):
        """Tests how much time it takes for v1 to calculate if the numbers 1 through 30000 are primes. The results are
        not saved, as this is only a test of the performance of the algorithm. Print the time required for the
        calculations in seconds."""

        start_time = time.time()

        for n in range(1, 30000):
            prime_numbers_v1(n)

        elapsed_time = round(time.time() - start_time, 3)

        print(f"v1, time required: {elapsed_time}")

    def test_v2_runtime(self):
        """Tests how much time it takes for v1 to calculate if the numbers 1 through 30000 are primes. The results are
        not saved, as this is only a test of the performance of the algorithm. Print the time required for the
        calculations in seconds."""

        start_time = time.time()

        for n in range(1, 30000):
            prime_numbers_v2(n)

        elapsed_time = round(time.time() - start_time, 3)

        print(f"v2, time required: {elapsed_time}")

    def test_v3_runtime(self):
        """Tests how much time it takes for v1 to calculate if the numbers 1 through 30000 are primes. The results are
        not saved, as this is only a test of the performance of the algorithm. Print the time required for the
        calculations in seconds."""

        start_time = time.time()

        for n in range(1, 30000):
            prime_numbers_v3(n)

        elapsed_time = round(time.time() - start_time, 3)

        print(f"v3, time required: {elapsed_time}")





if __name__ == '__main__':
    unittest.main()


