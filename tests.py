import unittest
from kurrency import Currency


class TestDBFunctions(unittest.TestCase):

    def test_get(self):
        self.assertEqual(Currency.get("TRY"), Currency.get("949"))
        self.assertEqual(Currency.get("949"), Currency.get("Turkish Lira"))

    def test_put(self):
        new_currency = Currency("XX", "XX", "XX", "XX", "XX", "XX", "XX", "XX", "XX", [])
        Currency.put(new_currency)
        self.assertEqual(Currency.get("XX"), new_currency)


if __name__ == "__main__":
    unittest.main()
