from decimal import Decimal
from kurrency import Currency
from kurrency import ExchangeRate
from kurrency import NoExchangeRateFound
import datetime
import unittest


def plugin_always_pi(*args, **kwargs):
    return ExchangeRate(rate=Decimal("3.1415"), add_to_cache=False, **kwargs)


class TestDBFunctions(unittest.TestCase):

    def test_get(self):
        self.assertEqual(Currency.get("TRY"), Currency.get("949"))
        self.assertEqual(Currency.get("949"), Currency.get("Turkish Lira"))

    def test_put(self):
        new_currency = Currency("XX", "100", "XX", "XX", "XX", "XX", "XX", "XX", 2, [])
        Currency.put(new_currency)
        self.assertEqual(Currency.get("XX"), new_currency)


class TestExchangeRateCachePluginFunctions(unittest.TestCase):

    def setUp(self):
        self.date_today = datetime.datetime.now().date()
        self.date_yesterday = self.date_today - datetime.timedelta(days=1)
        self.date_last_year = self.date_today - datetime.timedelta(days=365)
        self.time_noon = datetime.time(12,0,0)

    def test_init(self):
        """
        TODO: More tests
        """
        # Define some currencies:
        currencies = {"EUR": Currency.get("EUR"),
                      "USD": Currency.get("USD"),
                      "TRY": Currency.get("TRY")}

        # Define some rates:
        rates = {"USDTRY": ExchangeRate(currencies["USD"],
                                        currencies["TRY"],
                                        "2",),
                 "EURUSD": ExchangeRate(currencies["EUR"],
                                        currencies["USD"],
                                        "1",
                                        self.date_yesterday,
                                        self.time_noon,
                                        "close",
                                        "myass"),
                 "EURUSD_2": ExchangeRate(currencies["EUR"],
                                          currencies["USD"],
                                          "1",
                                          self.date_last_year,
                                          self.time_noon,
                                          "close",
                                          "myass",
                                          add_to_cache=False),
                 }

        # Now, start checing:
        self.assertEqual(ExchangeRate.plugin_cache(currencies["USD"],
                                                   currencies["TRY"]),
                         rates["USDTRY"])

        self.assertEqual(ExchangeRate.plugin_cache(currencies["USD"],
                                                   currencies["TRY"],
                                                   date=self.date_today),
                         rates["USDTRY"])

        self.assertEqual(ExchangeRate.plugin_cache(currencies["EUR"],
                                                   currencies["USD"],
                                                   self.date_yesterday,
                                                   self.time_noon,
                                                   "close",
                                                   "myass"),
                         rates["EURUSD"])

        self.assertRaises(NoExchangeRateFound, ExchangeRate.plugin_cache,
                          currencies["EUR"],
                          currencies["USD"],
                          self.date_last_year,
                          self.time_noon,
                          "close",
                          "myass"),


    def test_plugins(self):
        # Check an existing cached value:
        self.assertEqual(ExchangeRate.get(Currency.get("USD"),
                                          Currency.get("TRY")).rate,
                         Decimal("2"))

        # Add a new plugin:
        ExchangeRate.add_plugin("tests:plugin_always_pi")

        # Check new plugin:
        self.assertEqual(ExchangeRate.get(Currency.get("TRY"),
                                          Currency.get("USD")).rate,
                         Decimal("3.1415"))

if __name__ == "__main__":
    unittest.main()
