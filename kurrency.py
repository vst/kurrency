# -*- coding: utf-8 -*-
# Copyright (c) 2012, Vehbi Sinan Tunalioglu <vst@vsthost.com>
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
# - Redistributions of source code must retain the above copyright
#   notice, this list of conditions and the following disclaimer.
#
# - Redistributions in binary form must reproduce the above copyright
#   notice, this list of conditions and the following disclaimer in
#   the documentation and/or other materials provided with the
#   distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

__version__ = (0, 0, 0, "dev", 0)

from kountry import Country


class Currency(object):
    """
    Provides the canonical representation of a currency object and
    further functionality such as querying.
    """

    """
    Provides the currency database.
    """
    DB = {"index_code": dict(),
          "index_enum": dict(),
          "index_name": dict()}

    def __init__(self, code, enum, name, common_name, short_name, nickname,
                 symbol, short_symbol, decimal_points, countries):
        # Save object attributes:
        self.code = code
        self.enum = enum
        self.name = name
        self.common_name = common_name
        self.short_name = short_name
        self.nickname = nickname
        self.symbol = symbol
        self.short_symbol = short_symbol
        self.decimal_points = decimal_points
        self.countries = countries

    def __repr__(self):
        return self.name

    @classmethod
    def get(cls, identifier):
        """
        Queries the :attr:`Currency.DB` for the identifier provided
        and returns the currency object if found, ``None`` otherwise.
        """
        return cls.DB["index_code"].get(identifier) or \
               cls.DB["index_enum"].get(identifier) or \
               cls.DB["index_name"].get(identifier.upper())

    @classmethod
    def put(cls, currency):
        """
        Inserts or overrides a currency in the DB.

        Note that this method indexes every currency by its
        :attr:`code`, :attr:`enum` and :attr:`name` attributes.
        """
        cls.DB["index_code"][currency.code] = currency
        cls.DB["index_enum"][currency.enum] = currency
        cls.DB["index_name"][currency.name.upper()] = currency

#######################
# DATABASE POPULATION #
#######################

Currency.put(Currency("AED", "784",
                      "United Arab Emirates dirham",
                      "United Arab Emirates dirham",
                      "United Arab Emirates dirham",
                      "", "", "", "2",
                      [Country.get("AE")]))
Currency.put(Currency("AFN", "971",
                      "Afghan afghani",
                      "Afghan afghani",
                      "Afghan afghani",
                      "", "", "", "2",
                      [Country.get("AF")]))
Currency.put(Currency("ALL", "008",
                      "Albanian lek",
                      "Albanian lek",
                      "Albanian lek",
                      "", "", "", "2",
                      [Country.get("AL")]))
Currency.put(Currency("AMD", "051",
                      "Armenian dram",
                      "Armenian dram",
                      "Armenian dram",
                      "", "", "", "2",
                      [Country.get("AM")]))
Currency.put(Currency("ANG", "532",
                      "Netherlands Antillean guilder",
                      "Netherlands Antillean guilder",
                      "Netherlands Antillean guilder",
                      "", "", "", "2",
                      [Country.get("CW"), Country.get("SX")]))
Currency.put(Currency("AOA", "973",
                      "Angolan kwanza",
                      "Angolan kwanza",
                      "Angolan kwanza",
                      "", "", "", "2",
                      [Country.get("AO")]))
Currency.put(Currency("ARS", "032",
                      "Argentine peso",
                      "Argentine peso",
                      "Argentine peso",
                      "", "", "", "2",
                      [Country.get("AR")]))
Currency.put(Currency("AUD", "036",
                      "Australian dollar",
                      "Australian dollar",
                      "Australian dollar",
                      "", "", "", "2",
                      [Country.get("AU"), Country.get("CX"),
                       Country.get("CC"), Country.get("HM"),
                       Country.get("KI"), Country.get("NR"),
                       Country.get("NF"), Country.get("TV")]))
Currency.put(Currency("AWG", "533",
                      "Aruban florin",
                      "Aruban florin",
                      "Aruban florin",
                      "", "", "", "2",
                      [Country.get("AW")]))
Currency.put(Currency("AZN", "944",
                      "Azerbaijani manat",
                      "Azerbaijani manat",
                      "Azerbaijani manat",
                      "", "", "", "2",
                      [Country.get("AZ")]))
Currency.put(Currency("BAM", "977",
                      "Bosnia and Herzegovina convertible mark",
                      "Bosnia and Herzegovina convertible mark",
                      "Bosnia and Herzegovina convertible mark",
                      "", "", "", "2",
                      [Country.get("BA")]))
Currency.put(Currency("BBD", "052",
                      "Barbados dollar",
                      "Barbados dollar",
                      "Barbados dollar",
                      "", "", "", "2",
                      [Country.get("BB")]))
Currency.put(Currency("BDT", "050",
                      "Bangladeshi taka",
                      "Bangladeshi taka",
                      "Bangladeshi taka",
                      "", "", "", "2",
                      [Country.get("BD")]))
Currency.put(Currency("BGN", "975",
                      "Bulgarian lev",
                      "Bulgarian lev",
                      "Bulgarian lev",
                      "", "", "", "2",
                      [Country.get("BG")]))
Currency.put(Currency("BHD", "048",
                      "Bahraini dinar",
                      "Bahraini dinar",
                      "Bahraini dinar",
                      "", "", "", "3",
                      [Country.get("BH")]))
Currency.put(Currency("BIF", "108",
                      "Burundian franc",
                      "Burundian franc",
                      "Burundian franc",
                      "", "", "", "0",
                      [Country.get("BI")]))
Currency.put(Currency("BMD", "060",
                      "Bermudian dollar (customarily known as Bermuda dollar)",
                      "Bermudian dollar (customarily known as Bermuda dollar)",
                      "Bermudian dollar (customarily known as Bermuda dollar)",
                      "", "", "", "2",
                      [Country.get("BM")]))
Currency.put(Currency("BND", "096",
                      "Brunei dollar",
                      "Brunei dollar",
                      "Brunei dollar",
                      "", "", "", "2",
                      [Country.get("BN"), Country.get("SG")]))
Currency.put(Currency("BOB", "068",
                      "Boliviano",
                      "Boliviano",
                      "Boliviano",
                      "", "", "", "2",
                      [Country.get("BO")]))
Currency.put(Currency("BOV", "984",
                      "Bolivian Mvdol",
                      "Bolivian Mvdol",
                      "Bolivian Mvdol",
                      "", "", "", "2",
                      [Country.get("BO")]))
Currency.put(Currency("BRL", "986",
                      "Brazilian real",
                      "Brazilian real",
                      "Brazilian real",
                      "", "", "", "2",
                      [Country.get("BR")]))
Currency.put(Currency("BSD", "044",
                      "Bahamian dollar",
                      "Bahamian dollar",
                      "Bahamian dollar",
                      "", "", "", "2",
                      [Country.get("BS")]))
Currency.put(Currency("BTN", "064",
                      "Bhutanese ngultrum",
                      "Bhutanese ngultrum",
                      "Bhutanese ngultrum",
                      "", "", "", "2",
                      [Country.get("BT")]))
Currency.put(Currency("BWP", "072",
                      "Botswana pula",
                      "Botswana pula",
                      "Botswana pula",
                      "", "", "", "2",
                      [Country.get("BW")]))
Currency.put(Currency("BYR", "974",
                      "Belarusian ruble",
                      "Belarusian ruble",
                      "Belarusian ruble",
                      "", "", "", "0",
                      [Country.get("BY")]))
Currency.put(Currency("BZD", "084",
                      "Belize dollar",
                      "Belize dollar",
                      "Belize dollar",
                      "", "", "", "2",
                      [Country.get("BZ")]))
Currency.put(Currency("CAD", "124",
                      "Canadian dollar",
                      "Canadian dollar",
                      "Canadian dollar",
                      "", "", "", "2",
                      [Country.get("CA")]))
Currency.put(Currency("CDF", "976",
                      "Congolese franc",
                      "Congolese franc",
                      "Congolese franc",
                      "", "", "", "2",
                      [Country.get("CD")]))
Currency.put(Currency("CHE", "947",
                      "WIR Euro (complementary currency)",
                      "WIR Euro (complementary currency)",
                      "WIR Euro (complementary currency)",
                      "", "", "", "2",
                      [Country.get("CH")]))
Currency.put(Currency("CHF", "756",
                      "Swiss franc",
                      "Swiss franc",
                      "Swiss franc",
                      "", "", "", "2",
                      [Country.get("CH"), Country.get("LI")]))
Currency.put(Currency("CHW", "948",
                      "WIR Franc (complementary currency)",
                      "WIR Franc (complementary currency)",
                      "WIR Franc (complementary currency)",
                      "", "", "", "2",
                      [Country.get("CH")]))
Currency.put(Currency("CLF", "990",
                      "Unidad de Fomento",
                      "Unidad de Fomento",
                      "Unidad de Fomento",
                      "", "", "", "0",
                      [Country.get("CL")]))
Currency.put(Currency("CLP", "152",
                      "Chilean peso",
                      "Chilean peso",
                      "Chilean peso",
                      "", "", "", "0",
                      [Country.get("CL")]))
Currency.put(Currency("CNY", "156",
                      "Chinese yuan",
                      "Chinese yuan",
                      "Chinese yuan",
                      "", "", "", "2",
                      [Country.get("CN")]))
Currency.put(Currency("COP", "170",
                      "Colombian peso",
                      "Colombian peso",
                      "Colombian peso",
                      "", "", "", "2",
                      [Country.get("CO")]))
Currency.put(Currency("COU", "970",
                      "Unidad de Valor Real",
                      "Unidad de Valor Real",
                      "Unidad de Valor Real",
                      "", "", "", "2",
                      [Country.get("CO")]))
Currency.put(Currency("CRC", "188",
                      "Costa Rican colon",
                      "Costa Rican colon",
                      "Costa Rican colon",
                      "", "", "", "2",
                      [Country.get("CR")]))
Currency.put(Currency("CUC", "931",
                      "Cuban convertible peso",
                      "Cuban convertible peso",
                      "Cuban convertible peso",
                      "", "", "", "2",
                      [Country.get("CU")]))
Currency.put(Currency("CUP", "192",
                      "Cuban peso",
                      "Cuban peso",
                      "Cuban peso",
                      "", "", "", "2",
                      [Country.get("CU")]))
Currency.put(Currency("CVE", "132",
                      "Cape Verde escudo",
                      "Cape Verde escudo",
                      "Cape Verde escudo",
                      "", "", "", "0",
                      [Country.get("CV")]))
Currency.put(Currency("CZK", "203",
                      "Czech koruna",
                      "Czech koruna",
                      "Czech koruna",
                      "", "", "", "2",
                      [Country.get("CZ")]))
Currency.put(Currency("DJF", "262",
                      "Djiboutian franc",
                      "Djiboutian franc",
                      "Djiboutian franc",
                      "", "", "", "0",
                      [Country.get("DJ")]))
Currency.put(Currency("DKK", "208",
                      "Danish krone",
                      "Danish krone",
                      "Danish krone",
                      "", "", "", "2",
                      [Country.get("DK"), Country.get("FO"),
                       Country.get("GL")]))
Currency.put(Currency("DOP", "214",
                      "Dominican peso",
                      "Dominican peso",
                      "Dominican peso",
                      "", "", "", "2",
                      [Country.get("DO")]))
Currency.put(Currency("DZD", "012",
                      "Algerian dinar",
                      "Algerian dinar",
                      "Algerian dinar",
                      "", "", "", "2",
                      [Country.get("DZ")]))
Currency.put(Currency("EGP", "818",
                      "Egyptian pound",
                      "Egyptian pound",
                      "Egyptian pound",
                      "", "", "", "2",
                      [Country.get("EG")]))
Currency.put(Currency("ERN", "232",
                      "Eritrean nakfa",
                      "Eritrean nakfa",
                      "Eritrean nakfa",
                      "", "", "", "2",
                      [Country.get("ER")]))
Currency.put(Currency("ETB", "230",
                      "Ethiopian birr",
                      "Ethiopian birr",
                      "Ethiopian birr",
                      "", "", "", "2",
                      [Country.get("ET")]))
Currency.put(Currency("EUR", "978",
                      "Euro",
                      "Euro",
                      "Euro",
                      "", "", "", "2",
                      [Country.get("AD"), Country.get("AT"),
                       Country.get("BE"), Country.get("CY"),
                       Country.get("EE"), Country.get("FI"),
                       Country.get("FR"), Country.get("DE"),
                       Country.get("GR"), Country.get("IE"),
                       Country.get("IT"), Country.get("XK"),
                       Country.get("LU"), Country.get("MT"),
                       Country.get("MC"), Country.get("ME"),
                       Country.get("NL"), Country.get("PT"),
                       Country.get("SM"), Country.get("SK"),
                       Country.get("SI"), Country.get("ES"),
                       Country.get("VA")]))
Currency.put(Currency("FJD", "242",
                      "Fiji dollar",
                      "Fiji dollar",
                      "Fiji dollar",
                      "", "", "", "2",
                      [Country.get("FJ")]))
Currency.put(Currency("FKP", "238",
                      "Falkland Islands pound",
                      "Falkland Islands pound",
                      "Falkland Islands pound",
                      "", "", "", "2",
                      [Country.get("FK")]))
Currency.put(Currency("GBP", "826",
                      "Pound sterling",
                      "Pound sterling",
                      "Pound sterling",
                      "", "", "", "2",
                      [Country.get("GB"), Country.get("IM"),
                       Country.get("GS"), Country.get("IO")]))
Currency.put(Currency("GEL", "981",
                      "Georgian lari",
                      "Georgian lari",
                      "Georgian lari",
                      "", "", "", "2",
                      [Country.get("GE")]))
Currency.put(Currency("GHS", "936",
                      "Ghanaian cedi",
                      "Ghanaian cedi",
                      "Ghanaian cedi",
                      "", "", "", "2",
                      [Country.get("GH")]))
Currency.put(Currency("GIP", "292",
                      "Gibraltar pound",
                      "Gibraltar pound",
                      "Gibraltar pound",
                      "", "", "", "2",
                      [Country.get("GI")]))
Currency.put(Currency("GMD", "270",
                      "Gambian dalasi",
                      "Gambian dalasi",
                      "Gambian dalasi",
                      "", "", "", "2",
                      [Country.get("GM")]))
Currency.put(Currency("GNF", "324",
                      "Guinean franc",
                      "Guinean franc",
                      "Guinean franc",
                      "", "", "", "0",
                      [Country.get("GN")]))
Currency.put(Currency("GTQ", "320",
                      "Guatemalan quetzal",
                      "Guatemalan quetzal",
                      "Guatemalan quetzal",
                      "", "", "", "2",
                      [Country.get("GT")]))
Currency.put(Currency("GYD", "328",
                      "Guyanese dollar",
                      "Guyanese dollar",
                      "Guyanese dollar",
                      "", "", "", "2",
                      [Country.get("GY")]))
Currency.put(Currency("HKD", "344",
                      "Hong Kong dollar",
                      "Hong Kong dollar",
                      "Hong Kong dollar",
                      "", "", "", "2",
                      [Country.get("HK"), Country.get("MO")]))
Currency.put(Currency("HNL", "340",
                      "Honduran lempira",
                      "Honduran lempira",
                      "Honduran lempira",
                      "", "", "", "2",
                      [Country.get("HN")]))
Currency.put(Currency("HRK", "191",
                      "Croatian kuna",
                      "Croatian kuna",
                      "Croatian kuna",
                      "", "", "", "2",
                      [Country.get("HR")]))
Currency.put(Currency("HTG", "332",
                      "Haitian gourde",
                      "Haitian gourde",
                      "Haitian gourde",
                      "", "", "", "2",
                      [Country.get("HT")]))
Currency.put(Currency("HUF", "348",
                      "Hungarian forint",
                      "Hungarian forint",
                      "Hungarian forint",
                      "", "", "", "2",
                      [Country.get("HU")]))
Currency.put(Currency("IDR", "360",
                      "Indonesian rupiah",
                      "Indonesian rupiah",
                      "Indonesian rupiah",
                      "", "", "", "2",
                      [Country.get("ID")]))
Currency.put(Currency("ILS", "376",
                      "Israeli new sheqel",
                      "Israeli new sheqel",
                      "Israeli new sheqel",
                      "", "", "", "2",
                      [Country.get("IL"), Country.get("PS")]))
Currency.put(Currency("INR", "356",
                      "Indian rupee",
                      "Indian rupee",
                      "Indian rupee",
                      "", "", "", "2",
                      [Country.get("IN")]))
Currency.put(Currency("IQD", "368",
                      "Iraqi dinar",
                      "Iraqi dinar",
                      "Iraqi dinar",
                      "", "", "", "3",
                      [Country.get("IQ")]))
Currency.put(Currency("IRR", "364",
                      "Iranian rial",
                      "Iranian rial",
                      "Iranian rial",
                      "", "", "", "0",
                      [Country.get("IR")]))
Currency.put(Currency("ISK", "352",
                      "Icelandic króna",
                      "Icelandic króna",
                      "Icelandic króna",
                      "", "", "", "0",
                      [Country.get("IS")]))
Currency.put(Currency("JMD", "388",
                      "Jamaican dollar",
                      "Jamaican dollar",
                      "Jamaican dollar",
                      "", "", "", "2",
                      [Country.get("JM")]))
Currency.put(Currency("JOD", "400",
                      "Jordanian dinar",
                      "Jordanian dinar",
                      "Jordanian dinar",
                      "", "", "", "3",
                      [Country.get("JO")]))
Currency.put(Currency("JPY", "392",
                      "Japanese yen",
                      "Japanese yen",
                      "Japanese yen",
                      "", "", "", "0",
                      [Country.get("JP")]))
Currency.put(Currency("KES", "404",
                      "Kenyan shilling",
                      "Kenyan shilling",
                      "Kenyan shilling",
                      "", "", "", "2",
                      [Country.get("KE")]))
Currency.put(Currency("KGS", "417",
                      "Kyrgyzstani som",
                      "Kyrgyzstani som",
                      "Kyrgyzstani som",
                      "", "", "", "2",
                      [Country.get("KG")]))
Currency.put(Currency("KHR", "116",
                      "Cambodian riel",
                      "Cambodian riel",
                      "Cambodian riel",
                      "", "", "", "2",
                      [Country.get("KH")]))
Currency.put(Currency("KMF", "174",
                      "Comoro franc",
                      "Comoro franc",
                      "Comoro franc",
                      "", "", "", "0",
                      [Country.get("KM")]))
Currency.put(Currency("KPW", "408",
                      "North Korean won",
                      "North Korean won",
                      "North Korean won",
                      "", "", "", "0",
                      [Country.get("KP")]))
Currency.put(Currency("KRW", "410",
                      "South Korean won",
                      "South Korean won",
                      "South Korean won",
                      "", "", "", "0",
                      [Country.get("KR")]))
Currency.put(Currency("KWD", "414",
                      "Kuwaiti dinar",
                      "Kuwaiti dinar",
                      "Kuwaiti dinar",
                      "", "", "", "3",
                      [Country.get("KW")]))
Currency.put(Currency("KYD", "136",
                      "Cayman Islands dollar",
                      "Cayman Islands dollar",
                      "Cayman Islands dollar",
                      "", "", "", "2",
                      [Country.get("KY")]))
Currency.put(Currency("KZT", "398",
                      "Kazakhstani tenge",
                      "Kazakhstani tenge",
                      "Kazakhstani tenge",
                      "", "", "", "2",
                      [Country.get("KZ")]))
Currency.put(Currency("LAK", "418",
                      "Lao kip",
                      "Lao kip",
                      "Lao kip",
                      "", "", "", "0",
                      [Country.get("LA")]))
Currency.put(Currency("LBP", "422",
                      "Lebanese pound",
                      "Lebanese pound",
                      "Lebanese pound",
                      "", "", "", "0",
                      [Country.get("LB")]))
Currency.put(Currency("LKR", "144",
                      "Sri Lankan rupee",
                      "Sri Lankan rupee",
                      "Sri Lankan rupee",
                      "", "", "", "2",
                      [Country.get("LK")]))
Currency.put(Currency("LRD", "430",
                      "Liberian dollar",
                      "Liberian dollar",
                      "Liberian dollar",
                      "", "", "", "2",
                      [Country.get("LR")]))
Currency.put(Currency("LSL", "426",
                      "Lesotho loti",
                      "Lesotho loti",
                      "Lesotho loti",
                      "", "", "", "2",
                      [Country.get("LS")]))
Currency.put(Currency("LTL", "440",
                      "Lithuanian litas",
                      "Lithuanian litas",
                      "Lithuanian litas",
                      "", "", "", "2",
                      [Country.get("LT")]))
Currency.put(Currency("LVL", "428",
                      "Latvian lats",
                      "Latvian lats",
                      "Latvian lats",
                      "", "", "", "2",
                      [Country.get("LV")]))
Currency.put(Currency("LYD", "434",
                      "Libyan dinar",
                      "Libyan dinar",
                      "Libyan dinar",
                      "", "", "", "3",
                      [Country.get("LY")]))
Currency.put(Currency("MAD", "504",
                      "Moroccan dirham",
                      "Moroccan dirham",
                      "Moroccan dirham",
                      "", "", "", "2",
                      [Country.get("MA")]))
Currency.put(Currency("MDL", "498",
                      "Moldovan leu",
                      "Moldovan leu",
                      "Moldovan leu",
                      "", "", "", "2",
                      [Country.get("MD")]))
Currency.put(Currency("MGA", "969",
                      "Malagasy ariary",
                      "Malagasy ariary",
                      "Malagasy ariary",
                      "", "", "", "",
                      [Country.get("MG")]))
Currency.put(Currency("MKD", "807",
                      "Macedonian denar",
                      "Macedonian denar",
                      "Macedonian denar",
                      "", "", "", "2",
                      [Country.get("MK")]))
Currency.put(Currency("MMK", "104",
                      "Myanma kyat",
                      "Myanma kyat",
                      "Myanma kyat",
                      "", "", "", "0",
                      [Country.get("MM")]))
Currency.put(Currency("MNT", "496",
                      "Mongolian tugrik",
                      "Mongolian tugrik",
                      "Mongolian tugrik",
                      "", "", "", "2",
                      [Country.get("MN")]))
Currency.put(Currency("MOP", "446",
                      "Macanese pataca",
                      "Macanese pataca",
                      "Macanese pataca",
                      "", "", "", "2",
                      [Country.get("MO")]))
Currency.put(Currency("MRO", "478",
                      "Mauritanian ouguiya",
                      "Mauritanian ouguiya",
                      "Mauritanian ouguiya",
                      "", "", "", "",
                      [Country.get("MR")]))
Currency.put(Currency("MUR", "480",
                      "Mauritian rupee",
                      "Mauritian rupee",
                      "Mauritian rupee",
                      "", "", "", "2",
                      [Country.get("MU")]))
Currency.put(Currency("MVR", "462",
                      "Maldivian rufiyaa",
                      "Maldivian rufiyaa",
                      "Maldivian rufiyaa",
                      "", "", "", "2",
                      [Country.get("MV")]))
Currency.put(Currency("MWK", "454",
                      "Malawian kwacha",
                      "Malawian kwacha",
                      "Malawian kwacha",
                      "", "", "", "2",
                      [Country.get("MW")]))
Currency.put(Currency("MXN", "484",
                      "Mexican peso",
                      "Mexican peso",
                      "Mexican peso",
                      "", "", "", "2",
                      [Country.get("MX")]))
Currency.put(Currency("MXV", "979",
                      "Mexican Unidad de Inversion (UDI)",
                      "Mexican Unidad de Inversion (UDI)",
                      "Mexican Unidad de Inversion (UDI)",
                      "", "", "", "2",
                      [Country.get("MX")]))
Currency.put(Currency("MYR", "458",
                      "Malaysian ringgit",
                      "Malaysian ringgit",
                      "Malaysian ringgit",
                      "", "", "", "2",
                      [Country.get("MY")]))
Currency.put(Currency("MZN", "943",
                      "Mozambican metical",
                      "Mozambican metical",
                      "Mozambican metical",
                      "", "", "", "2",
                      [Country.get("MZ")]))
Currency.put(Currency("NAD", "516",
                      "Namibian dollar",
                      "Namibian dollar",
                      "Namibian dollar",
                      "", "", "", "2",
                      [Country.get("NA")]))
Currency.put(Currency("NGN", "566",
                      "Nigerian naira",
                      "Nigerian naira",
                      "Nigerian naira",
                      "", "", "", "2",
                      [Country.get("NG")]))
Currency.put(Currency("NIO", "558",
                      "Nicaraguan córdoba",
                      "Nicaraguan córdoba",
                      "Nicaraguan córdoba",
                      "", "", "", "2",
                      [Country.get("NI")]))
Currency.put(Currency("NOK", "578",
                      "Norwegian krone",
                      "Norwegian krone",
                      "Norwegian krone",
                      "", "", "", "2",
                      [Country.get("NO"), Country.get("SJ"),
                       Country.get("BV")]))
Currency.put(Currency("NPR", "524",
                      "Nepalese rupee",
                      "Nepalese rupee",
                      "Nepalese rupee",
                      "", "", "", "2",
                      [Country.get("NP")]))
Currency.put(Currency("NZD", "554",
                      "New Zealand dollar",
                      "New Zealand dollar",
                      "New Zealand dollar",
                      "", "", "", "2",
                      [Country.get("CK"), Country.get("NZ"),
                       Country.get("NU"), Country.get("PN"),
                       Country.get("TK")]))
Currency.put(Currency("OMR", "512",
                      "Omani rial",
                      "Omani rial",
                      "Omani rial",
                      "", "", "", "3",
                      [Country.get("OM")]))
Currency.put(Currency("PAB", "590",
                      "Panamanian balboa",
                      "Panamanian balboa",
                      "Panamanian balboa",
                      "", "", "", "2",
                      [Country.get("PA")]))
Currency.put(Currency("PEN", "604",
                      "Peruvian nuevo sol",
                      "Peruvian nuevo sol",
                      "Peruvian nuevo sol",
                      "", "", "", "2",
                      [Country.get("PE")]))
Currency.put(Currency("PGK", "598",
                      "Papua New Guinean kina",
                      "Papua New Guinean kina",
                      "Papua New Guinean kina",
                      "", "", "", "2",
                      [Country.get("PG")]))
Currency.put(Currency("PHP", "608",
                      "Philippine peso",
                      "Philippine peso",
                      "Philippine peso",
                      "", "", "", "2",
                      [Country.get("PH")]))
Currency.put(Currency("PKR", "586",
                      "Pakistani rupee",
                      "Pakistani rupee",
                      "Pakistani rupee",
                      "", "", "", "2",
                      [Country.get("PK")]))
Currency.put(Currency("PLN", "985",
                      "Polish złoty",
                      "Polish złoty",
                      "Polish złoty",
                      "", "", "", "2",
                      [Country.get("PL")]))
Currency.put(Currency("PYG", "600",
                      "Paraguayan guaraní",
                      "Paraguayan guaraní",
                      "Paraguayan guaraní",
                      "", "", "", "0",
                      [Country.get("PY")]))
Currency.put(Currency("QAR", "634",
                      "Qatari riyal",
                      "Qatari riyal",
                      "Qatari riyal",
                      "", "", "", "2",
                      [Country.get("QA")]))
Currency.put(Currency("RON", "946",
                      "Romanian new leu",
                      "Romanian new leu",
                      "Romanian new leu",
                      "", "", "", "2",
                      [Country.get("RO")]))
Currency.put(Currency("RSD", "941",
                      "Serbian dinar",
                      "Serbian dinar",
                      "Serbian dinar",
                      "", "", "", "2",
                      [Country.get("RS")]))
Currency.put(Currency("RUB", "643",
                      "Russian rouble",
                      "Russian rouble",
                      "Russian rouble",
                      "", "", "", "2",
                      [Country.get("RU")]))
Currency.put(Currency("RWF", "646",
                      "Rwandan franc",
                      "Rwandan franc",
                      "Rwandan franc",
                      "", "", "", "0",
                      [Country.get("RW")]))
Currency.put(Currency("SAR", "682",
                      "Saudi riyal",
                      "Saudi riyal",
                      "Saudi riyal",
                      "", "", "", "2",
                      [Country.get("SA")]))
Currency.put(Currency("SBD", "090",
                      "Solomon Islands dollar",
                      "Solomon Islands dollar",
                      "Solomon Islands dollar",
                      "", "", "", "2",
                      [Country.get("SB")]))
Currency.put(Currency("SCR", "690",
                      "Seychelles rupee",
                      "Seychelles rupee",
                      "Seychelles rupee",
                      "", "", "", "2",
                      [Country.get("SC")]))
Currency.put(Currency("SDG", "938",
                      "Sudanese pound",
                      "Sudanese pound",
                      "Sudanese pound",
                      "", "", "", "2",
                      [Country.get("SD")]))
Currency.put(Currency("SEK", "752",
                      "Swedish krona/kronor",
                      "Swedish krona/kronor",
                      "Swedish krona/kronor",
                      "", "", "", "2",
                      [Country.get("SE")]))
Currency.put(Currency("SGD", "702",
                      "Singapore dollar",
                      "Singapore dollar",
                      "Singapore dollar",
                      "", "", "", "2",
                      [Country.get("SG"), Country.get("BN")]))
Currency.put(Currency("SHP", "654",
                      "Saint Helena pound",
                      "Saint Helena pound",
                      "Saint Helena pound",
                      "", "", "", "2",
                      [Country.get("SH")]))
Currency.put(Currency("SLL", "694",
                      "Sierra Leonean leone",
                      "Sierra Leonean leone",
                      "Sierra Leonean leone",
                      "", "", "", "0",
                      [Country.get("SL")]))
Currency.put(Currency("SOS", "706",
                      "Somali shilling",
                      "Somali shilling",
                      "Somali shilling",
                      "", "", "", "2",
                      [Country.get("SO")]))
Currency.put(Currency("SRD", "968",
                      "Surinamese dollar",
                      "Surinamese dollar",
                      "Surinamese dollar",
                      "", "", "", "2",
                      [Country.get("SR")]))
Currency.put(Currency("SSP", "728",
                      "South Sudanese pound",
                      "South Sudanese pound",
                      "South Sudanese pound",
                      "", "", "", "2",
                      [Country.get("SS")]))
Currency.put(Currency("STD", "678",
                      "São Tomé and Príncipe dobra",
                      "São Tomé and Príncipe dobra",
                      "São Tomé and Príncipe dobra",
                      "", "", "", "0",
                      [Country.get("ST")]))
Currency.put(Currency("SYP", "760",
                      "Syrian pound",
                      "Syrian pound",
                      "Syrian pound",
                      "", "", "", "2",
                      [Country.get("SY")]))
Currency.put(Currency("SZL", "748",
                      "Swazi lilangeni",
                      "Swazi lilangeni",
                      "Swazi lilangeni",
                      "", "", "", "2",
                      [Country.get("SZ")]))
Currency.put(Currency("THB", "764",
                      "Thai baht",
                      "Thai baht",
                      "Thai baht",
                      "", "", "", "2",
                      [Country.get("TH")]))
Currency.put(Currency("TJS", "972",
                      "Tajikistani somoni",
                      "Tajikistani somoni",
                      "Tajikistani somoni",
                      "", "", "", "2",
                      [Country.get("TJ")]))
Currency.put(Currency("TMT", "934",
                      "Turkmenistani manat",
                      "Turkmenistani manat",
                      "Turkmenistani manat",
                      "", "", "", "2",
                      [Country.get("TM")]))
Currency.put(Currency("TND", "788",
                      "Tunisian dinar",
                      "Tunisian dinar",
                      "Tunisian dinar",
                      "", "", "", "3",
                      [Country.get("TN")]))
Currency.put(Currency("TOP", "776",
                      "Tongan paʻanga",
                      "Tongan paʻanga",
                      "Tongan paʻanga",
                      "", "", "", "2",
                      [Country.get("TO")]))
Currency.put(Currency("TRY", "949",
                      "Turkish lira",
                      "Turkish lira",
                      "Turkish lira",
                      "", "", "", "2",
                      [Country.get("TR")]))
Currency.put(Currency("TTD", "780",
                      "Trinidad and Tobago dollar",
                      "Trinidad and Tobago dollar",
                      "Trinidad and Tobago dollar",
                      "", "", "", "2",
                      [Country.get("TT")]))
Currency.put(Currency("TWD", "901",
                      "New Taiwan dollar",
                      "New Taiwan dollar",
                      "New Taiwan dollar",
                      "", "", "", "2",
                      [Country.get("TW")]))
Currency.put(Currency("TZS", "834",
                      "Tanzanian shilling",
                      "Tanzanian shilling",
                      "Tanzanian shilling",
                      "", "", "", "2",
                      [Country.get("TZ")]))
Currency.put(Currency("UAH", "980",
                      "Ukrainian hryvnia",
                      "Ukrainian hryvnia",
                      "Ukrainian hryvnia",
                      "", "", "", "2",
                      [Country.get("UA")]))
Currency.put(Currency("UGX", "800",
                      "Ugandan shilling",
                      "Ugandan shilling",
                      "Ugandan shilling",
                      "", "", "", "2",
                      [Country.get("UG")]))
Currency.put(Currency("USD", "840",
                      "United States dollar",
                      "United States dollar",
                      "United States dollar",
                      "", "", "", "2",
                      [Country.get("AS"), Country.get("BB"),
                       Country.get("BM"), Country.get("IO"),
                       Country.get("VG"), Country.get("EC"),
                       Country.get("SV"), Country.get("GU"),
                       Country.get("HT"), Country.get("MH"),
                       Country.get("FM"), Country.get("MP"),
                       Country.get("PW"), Country.get("PA"),
                       Country.get("PR"), Country.get("TC"),
                       Country.get("US"), Country.get("VI"),
                       Country.get("ZW")]))
Currency.put(Currency("USN", "997",
                      "United States dollar (next day)",
                      "United States dollar (next day)",
                      "United States dollar (next day)",
                      "", "", "", "2",
                      [Country.get("US")]))
Currency.put(Currency("USS", "998",
                      "United States dollar (same day)",
                      "United States dollar (same day)",
                      "United States dollar (same day)",
                      "", "", "", "2",
                      [Country.get("US")]))
Currency.put(Currency("UYI", "940",
                      "Uruguay Peso en Unidades Indexadas (URUIURUI)",
                      "Uruguay Peso en Unidades Indexadas (URUIURUI)",
                      "Uruguay Peso en Unidades Indexadas (URUIURUI)",
                      "", "", "", "0",
                      [Country.get("UY")]))
Currency.put(Currency("UYU", "858",
                      "Uruguayan peso",
                      "Uruguayan peso",
                      "Uruguayan peso",
                      "", "", "", "2",
                      [Country.get("UY")]))
Currency.put(Currency("UZS", "860",
                      "Uzbekistan som",
                      "Uzbekistan som",
                      "Uzbekistan som",
                      "", "", "", "2",
                      [Country.get("UZ")]))
Currency.put(Currency("VEF", "937",
                      "Venezuelan bolívar fuerte",
                      "Venezuelan bolívar fuerte",
                      "Venezuelan bolívar fuerte",
                      "", "", "", "2",
                      [Country.get("VE")]))
Currency.put(Currency("VND", "704",
                      "Vietname dong",
                      "Vietname dong",
                      "Vietname dong",
                      "", "", "", "0",
                      [Country.get("VN")]))
Currency.put(Currency("VUV", "548",
                      "Vanuatu vatu",
                      "Vanuatu vatu",
                      "Vanuatu vatu",
                      "", "", "", "0",
                      [Country.get("VU")]))
Currency.put(Currency("WST", "882",
                      "Samoan tala",
                      "Samoan tala",
                      "Samoan tala",
                      "", "", "", "2",
                      [Country.get("WS")]))
Currency.put(Currency("XAF", "950",
                      "CFA franc BEAC",
                      "CFA franc BEAC",
                      "CFA franc BEAC",
                      "", "", "", "0",
                      [Country.get("CM"), Country.get("CF"),
                       Country.get("CG"), Country.get("TD"),
                       Country.get("GQ"), Country.get("GA")]))
Currency.put(Currency("XAG", "961",
                      "Silver (one troy ounce)",
                      "Silver (one troy ounce)",
                      "Silver (one troy ounce)",
                      "", "", "", "0",
                      []))
Currency.put(Currency("XAU", "959",
                      "Gold (one troy ounce)",
                      "Gold (one troy ounce)",
                      "Gold (one troy ounce)",
                      "", "", "", "0",
                      []))
Currency.put(Currency("XBA", "955",
                      "European Composite Unit (EURCO)",
                      "European Composite Unit (EURCO)",
                      "European Composite Unit (EURCO)",
                      "", "", "", "0",
                      []))
Currency.put(Currency("XBB", "956",
                      "European Monetary Unit (E.M.U.-6)",
                      "European Monetary Unit (E.M.U.-6)",
                      "European Monetary Unit (E.M.U.-6)",
                      "", "", "", "0",
                      []))
Currency.put(Currency("XBC", "957",
                      "European Unit of Account 9 (E.U.A.-9)",
                      "European Unit of Account 9 (E.U.A.-9)",
                      "European Unit of Account 9 (E.U.A.-9)",
                      "", "", "", "0",
                      []))
Currency.put(Currency("XBD", "958",
                      "European Unit of Account 17 (E.U.A.-17)",
                      "European Unit of Account 17 (E.U.A.-17)",
                      "European Unit of Account 17 (E.U.A.-17)",
                      "", "", "", "0",
                      []))
Currency.put(Currency("XCD", "951",
                      "East Caribbean dollar",
                      "East Caribbean dollar",
                      "East Caribbean dollar",
                      "", "", "", "2",
                      [Country.get("AI"), Country.get("AG"),
                       Country.get("DM"), Country.get("GD"),
                       Country.get("MS"), Country.get("KN"),
                       Country.get("LC"), Country.get("VC")]))
Currency.put(Currency("XDR", "960",
                      "Special drawing rights",
                      "Special drawing rights",
                      "Special drawing rights",
                      "", "", "", "0",
                      []))
Currency.put(Currency("XFU", "None",
                      "UIC franc (special settlement currency)",
                      "UIC franc (special settlement currency)",
                      "UIC franc (special settlement currency)",
                      "", "", "", "0",
                      []))
Currency.put(Currency("XOF", "952",
                      "CFA Franc BCEAO",
                      "CFA Franc BCEAO",
                      "CFA Franc BCEAO",
                      "", "", "", "0",
                      [Country.get("BJ"), Country.get("BF"),
                       Country.get("GW"), Country.get("ML"),
                       Country.get("NE"), Country.get("SN"),
                       Country.get("TG")]))
Currency.put(Currency("XPD", "964",
                      "Palladium (one troy ounce)",
                      "Palladium (one troy ounce)",
                      "Palladium (one troy ounce)",
                      "", "", "", "0",
                      []))
Currency.put(Currency("XPF", "953",
                      "CFP franc",
                      "CFP franc",
                      "CFP franc",
                      "", "", "", "0",
                      [Country.get("PF"), Country.get("NC"),
                       Country.get("WF")]))
Currency.put(Currency("XPT", "962",
                      "Platinum (one troy ounce)",
                      "Platinum (one troy ounce)",
                      "Platinum (one troy ounce)",
                      "", "", "", "0",
                      []))
Currency.put(Currency("XTS", "963",
                      "Code reserved for testing purposes",
                      "Code reserved for testing purposes",
                      "Code reserved for testing purposes",
                      "", "", "", "0",
                      []))
Currency.put(Currency("XXX", "999",
                      "No currency",
                      "No currency",
                      "No currency",
                      "", "", "", "0",
                      []))
Currency.put(Currency("YER", "886",
                      "Yemeni rial",
                      "Yemeni rial",
                      "Yemeni rial",
                      "", "", "", "2",
                      [Country.get("YE")]))
Currency.put(Currency("ZAR", "710",
                      "South African rand",
                      "South African rand",
                      "South African rand",
                      "", "", "", "2",
                      [Country.get("ZA")]))
Currency.put(Currency("ZMK", "894",
                      "Zambian kwacha",
                      "Zambian kwacha",
                      "Zambian kwacha",
                      "", "", "", "2",
                      [Country.get("ZM")]))
Currency.put(Currency("ZWL", "932",
                      "Zimbabwe dollar",
                      "Zimbabwe dollar",
                      "Zimbabwe dollar",
                      "", "", "", "2",
                      [Country.get("ZW")]))
