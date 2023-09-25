import decimal
from decimal import *

class Product:

    # Constants
    DEFAULT_BARCODE = "BARCODE NOT SET"
    DEFAULT_NAME = "NAME NOT SET"
    DEFAULT_PRICE = Decimal(0)

    # Constructor
    def __init__(self, barcode, name, price):
        self.set_barcode(barcode)
        self.set_name(name)
        self.set_price(price)

    # Getters
    def get_barcode(self):
        return self.__barcode

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price

    # Setters
    def set_barcode(self, barcode):
        # Verify length = 3
        if len(barcode) != 3:
            self.__barcode = Product.DEFAULT_BARCODE
            return

        # Verify is number
        if not barcode.isnumeric():
            self.__barcode = Product.DEFAULT_BARCODE
            return

        # Set valid barcode
        self.__barcode = barcode

    def set_name(self, name):
        name = name.strip()

        # verify name is minimum 3 letters long
        if len(name) < 3:
            self.__name = Product.DEFAULT_NAME
            return

        # Set valid name
        self.__name = name

    def set_price(self, price):
        # # Verify price is not empty
        if len(price) < 1:
            self.__price = Product.DEFAULT_PRICE
            return

        # Convert price input to decimal
        try:
            price = Decimal(price)
        except ValueError:
            self.__price = Product.DEFAULT_PRICE
            return
        except TypeError:
            self.__price = Product.DEFAULT_PRICE
            return
        except InvalidOperation:
            self.__price = Product.DEFAULT_PRICE
            return

        # Verify positive number
        if price < 0:
            self.__price = Product.DEFAULT_PRICE
            return

        # Round price to 2 decimal places
        price = price.quantize(decimal.Decimal('0.00'))

        # Set verified price
        self.__price = price

    def __str__(self):
        details = f"\n{super().__str__()}"
        details += f"\n["
        details += f"\n\tBarcode: {self.__barcode}"
        details += f"\n\tName: {self.__name}"
        details += f"\n\tPrice: {self.__price}"
        details += f"\n]"
        return details
