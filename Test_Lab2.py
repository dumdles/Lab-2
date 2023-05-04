import unittest
import Lab2 as temp
import statistics


class MyTestCase(unittest.TestCase):
    def test_something(self):
        temp1 = [1, 2, 3, 4, 5]

        self.assertEqual(temp.find_min_max(temp1), (1, 5))  # add assertion here
        self.assertEqual(temp.calc_average(temp1), 3)
        self.assertEqual(temp.calc_median_temperature(temp1), 3)


if __name__ == '_main_':
    unittest.main()