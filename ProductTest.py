import unittest
from CheckoutRegister import CheckoutRegister
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

        self.checkout = CheckoutRegister()

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

    def test_checkout_init(self):
        self.assertEqual(self.checkout.get_current_transaction_list(), [])
        self.assertEqual(self.checkout.get_current_transaction_total(), 0)
        self.assertEqual(self.checkout.get_current_transaction_payments_made(), 0)
        self.assertEqual(self.checkout.get_current_transaction_payment_due(), 0)

    def test_scan_item(self):
        # Scan in product Garlic Paste
        self.checkout.scan_item("001")

        # verify correct item added to transaction list
        product = self.checkout.get_current_transaction_list()[0]
        self.assertEqual(product.get_name(), "Garlic Paste")

        # verify transaction total and payment due updated
        price = Decimal(0.43)
        price = price.quantize(decimal.Decimal('0.00'))
        self.assertEqual(self.checkout.get_current_transaction_payment_due(), price)
        self.assertEqual(self.checkout.get_current_transaction_total(), price)

        # Scan in bad product code
        self.checkout.reset_register()
        self.checkout.scan_item("111")

        # Confirm no product added to transaction list
        number_of_products_scanned = len(self.checkout.get_current_transaction_list())
        self.assertEqual(number_of_products_scanned, 0)

        # Confirm payment due and transaction total not modified from bad product input
        self.assertEqual(self.checkout.get_current_transaction_payment_due(), 0)
        self.assertEqual(self.checkout.get_current_transaction_total(), 0)

    def test_accept_payment(self):
        # Scan in product Garlic Paste setting amount owed to 0.43
        self.checkout.scan_item("001")

        # Pay 5 dollars setting payment due to -4.57
        self.checkout.accept_payment("5")
        amount = Decimal(-4.57)
        amount = amount.quantize(decimal.Decimal('0.00'))
        self.assertEqual(self.checkout.get_current_transaction_payment_due(), amount)

        # Reset register
        self.checkout.reset_register()

        # scan in multiple products setting price to 23.23
        self.checkout.scan_item("017")
        self.checkout.scan_item("011")
        self.checkout.scan_item("013")
        self.checkout.scan_item("015")
        amount = Decimal(23.23)
        amount = amount.quantize(decimal.Decimal('0.00'))
        self.assertEqual(self.checkout.get_current_transaction_payment_due(), amount)

        # pay 5 dollars, setting amount due to 18.23
        self.checkout.accept_payment("5")
        amount = Decimal(18.23)
        amount = amount.quantize(decimal.Decimal('0.00'))
        self.assertEqual(self.checkout.get_current_transaction_payment_due(), amount)

        # pay 5 cents, setting amount due to 18.18
        self.checkout.accept_payment("0.05")
        amount = Decimal(18.18)
        amount = amount.quantize(decimal.Decimal('0.00'))
        self.assertEqual(self.checkout.get_current_transaction_payment_due(), amount)

        # pay 20 dollar, setting amount to -1.82 (change to pay customer0
        self.checkout.accept_payment("20")
        amount = Decimal(-1.82)
        amount = amount.quantize(decimal.Decimal('0.00'))
        self.assertEqual(self.checkout.get_current_transaction_payment_due(), amount)



if __name__ == '__main__':
    unittest.main()
