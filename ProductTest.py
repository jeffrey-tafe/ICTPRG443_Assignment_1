import unittest
from Product import Product
import decimal
from decimal import *


class ProductTest(unittest.TestCase):

    def setUp(self):
        self.product1 = Product("00102as", "G", "0.4333")
        self.product2 = Product("002", "Garlic Paste", "0.4333")
        self.product3 = Product("", "Garlic Paste", "two dollars")
        self.product4 = Product("004", "", "034")
        self.product5 = Product("001", "Garlic Paste", "8.7")

    def test_barcode_invalid(self):
        result = self.product1.get_barcode() == "BARCODE NOT SET"
        self.assertTrue(result)

    def test_barcode_invalid_empty(self):
        result = self.product3.get_barcode() == "BARCODE NOT SET"
        self.assertTrue(result)

    def test_barcode_valid(self):
        result = self.product2.get_barcode() == "002"
        self.assertTrue(result)

    def test_name_invalid(self):
        result = self.product1.get_name() == "NAME NOT SET"
        self.assertTrue(result)

    def test_name_invalid_empty(self):
        result = self.product4.get_name() == "NAME NOT SET"
        self.assertTrue(result)

    def test_name_valid(self):
        result = self.product2.get_name() == "Garlic Paste"
        self.assertTrue(result)

    def test_price_invalid(self):
        result = self.product3.get_price() == 0
        self.assertTrue(result)

    def test_price_invalid_empty(self):
        result = self.product3.get_price() == 0
        self.assertTrue(result)

    def test_price_valid(self):
        test_value = Decimal(8.70)
        test_value = test_value.quantize(decimal.Decimal('0.00'))
        result = self.product5.get_price() == test_value
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()
