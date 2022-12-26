import unittest
import money


class Tests(unittest.TestCase):

    def test_convert_tryto_rub(self):
        self.assertEqual("10 TRY = 37.01657 RUB", money.convert_TRYtoRub(10))
        self.assertEqual("1 TRY = 3.701657 RUB", money.convert_TRYtoRub(1))
        self.assertEqual("0 TRY = 0.0 RUB", money.convert_TRYtoRub(0))
        self.assertEqual("25 TRY = 92.541425 RUB", money.convert_TRYtoRub(25))

    def test_convert_rubto_try(self):
        self.assertEqual("10 RUB = 2.7021499999999996 TRY", money.convert_RubtoTry(10))
        self.assertEqual("1 RUB = 0.270215 TRY", money.convert_RubtoTry(1))
        self.assertEqual("0 RUB = 0.0 TRY", money.convert_RubtoTry(0))
        self.assertEqual("12 RUB = 3.24258 TRY", money.convert_RubtoTry(12))

    def test_random_money(self):
        currencies = ["USD", "EUR", "AUD", "CAD", "BYN", "KZT", "UAH", "GBP", "CZK", "CHF", "JPY", "MGA", "AFN", "ZAR",
                      "XOF", "SCR", "RWF", "RUB", "TRY", "ANG", "BHD", "CAD", "DZD", "GTQ", "HNL", "KGS", "LRD", "MVR",
                      "NZD", "PHP", "RSD", "SGD", "SZL"]
        out1, out2, out3, out4, out5 = money.random_money()
        self.assertTrue(currencies.__contains__(out1))
        self.assertTrue(currencies.__contains__(out2))
        self.assertTrue(out3 in range(0, 32))
        self.assertTrue(out4 in range(0, 32))
        self.assertTrue(out5 in range(0, 1000000))


if __name__ == '__main__':
    unittest.main()
