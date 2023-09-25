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

    def test_get_barcode(self):
        self.assertEqual(self.product1.get_barcode(), "BARCODE NOT SET")
        self.assertEqual(self.product3.get_barcode(), "BARCODE NOT SET")
        self.assertEqual(self.product2.get_barcode(), "002")

    def test_get_name(self):
        self.assertEqual(self.product1.get_name(),"NAME NOT SET")
        self.assertEqual(self.product4.get_name(), "NAME NOT SET")
        self.assertEqual(self.product2.get_name(), "Garlic Paste")

    def test_get_price(self):
        self.assertEqual(self.product3.get_price(), 0)
        self.assertEqual(self.product3.get_price(), 0)
        test_value = Decimal(8.70)
        test_value = test_value.quantize(decimal.Decimal('0.00'))
        self.assertEqual(self.product5.get_price(), test_value)


if __name__ == '__main__':
    unittest.main()
