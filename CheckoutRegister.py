from decimal import *
from Product import Product
import os

class CheckoutRegister:

    # Constructor
    def __init__(self):
        # store items purchased in this transaction
        self.__current_transaction_list = []

        # store running total for final price
        self.__current_transaction_total = Decimal(0)

        # store payments made so far
        self.__current_transaction_payment_due = Decimal(0)

        # get and store product list as part of instantiation
        self.__load_products()

    # Getters
    def __load_products(self):
        self.__product_list = []

        # Open products.txt with context manager
        with open('products.txt', 'r') as products:
            for line in products:

                # Split the line into fields
                fields = line.strip().split(';')

                # Get named properties from each field in list
                barcode, name, price = fields

                # Create product object from properties
                product = Product(barcode, name, price)

                # Add product to products list
                self.__product_list.append(product)

    # Setters

    # Methods

    # scan item from input barcode
    def scan_item(self, barcode):
        barcode = barcode.strip()

        # If no input, exit
        if len(barcode) < 1:
            CheckoutRegister.__show_error_barcode()
            return

        # If invalid input, exit
        if not self.__is_valid_barcode(barcode):
            CheckoutRegister.__show_error_barcode()
            return

        # get product
        product = self.__get_product(barcode)

        # add product to current transaction
        self.__current_transaction_list.append(product)

        # add product to current transaction total
        self.__current_transaction_total += product.get_price()

        # display product name, price and subtotal
        print(f"Item: {product.get_name()} | PRICE: ${product.get_price()} | SUBTOTAL: {self.__current_transaction_total}")

    # accept payment and subtract from total
    def accept_payment(self, amount_paid):
        pass

    def print_receipt(self):
        pass

    def save_transaction(self, date, barcode, amount):
        pass

    @staticmethod
    def __show_error_barcode():
        print("ERROR!! Scanned barcode is incorrect")

    @staticmethod
    def cls():
        os.system('cls' if os.name == 'nt' else 'clear')

    def get_product_list(self):
        return self.__product_list

    # return product object from input barcode
    # return none if not found
    def __get_product(self, barcode):
        for product in self.__product_list:
            if product.get_barcode() == barcode:
                return product


    def start(self):
        print("\n\nWelcome to the Self Service Checkout.")

        continue_scan = True

        while continue_scan:
            self.prompt_barcode()
            continue_scan = self.prompt_another_item()

    def prompt_barcode(self):
        barcode = input("\nPlease enter the barcode of your item: ")
        self.scan_item(barcode)

    def __is_valid_barcode(self, barcode):
        for product in self.__product_list:
            if product.get_barcode() == barcode:
                return True
        return False

    def prompt_another_item(self):
        response = input("Would you like to scan another item? (Y/N): ")
        response = response.strip()

        if response.lower() == "y":
            return True
        if response.lower() == "n":
            return False
        print("Response not recognised. Please try again.")
        self.prompt_another_item()



