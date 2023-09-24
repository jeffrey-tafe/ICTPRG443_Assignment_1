from decimal import *
from Product import Product
import os
from tabulate import tabulate



class CheckoutRegister:

    # Constructor
    def __init__(self):
        # store items purchased in this transaction
        self.__current_transaction_list = []

        # store running total for final price
        self.__current_transaction_total = Decimal(0)

        # store payments made so far and owing
        self.__current_transaction_payments_made = Decimal(0)
        self.__current_transaction_payment_due = Decimal(0)

        # get and store product list as part of instantiation
        self.__load_products()

    # Methods

    # accept payment and subtract from total
    def accept_payment(self, amount_paid):
        self.__current_transaction_payments_made += amount_paid
        self.__current_transaction_payment_due -= amount_paid

    @staticmethod
    def cls():
        os.system('cls' if os.name == 'nt' else 'clear')

    # return product object from input barcode
    def __get_product(self, barcode):
        for product in self.__product_list:
            if product.get_barcode() == barcode:
                return product

    # return product list
    def __get_product_list(self):
        return self.__product_list

    # return if payment complete
    def __is_payment_complete(self):
        return self.__current_transaction_payment_due > 0

    # verify barcode
    def __is_valid_barcode(self, barcode):

        # If no input, exit
        if len(barcode) < 1:
            return False

        for product in self.__product_list:
            if product.get_barcode() == barcode:
                return True
        return False

    # verify payment amount
    def __is_valid_payment(self, payment):
        # If no input, exit
        if len(payment) < 1:
            return False

        # if input can't be cast as decimal, exit
        try:
            payment_decimal = Decimal(payment)

            # If less than 0, return False
            if payment_decimal < 0:
                return False

        except ValueError:
            return False
        except TypeError:
            return False
        except InvalidOperation:
            return False

        # Check no more than 2 decimal places
        if '.' in payment:
            # Split string at decimal point
            integer_part, decimal_part = payment.split('.')

            # if more than 2 decimal places, return False
            if len(decimal_part) > 2:
                return False

        # All checks passed, return true
        return True

    # load product list from file
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

    # Build receipt string with tabulate then output
    def __print_receipt(self):
        # Receipt header
        receipt = "\n\nFINAL RECEIPT\n\n"

        headers = ["ITEM", "PRICE"]
        data = []

        for product in self.__current_transaction_list:
            data.append([product.get_name(), f"${product.get_price()}"])

        data.append(["", ""])
        data.append(["TOTAL", f"${self.__current_transaction_total}"])

        data.append(["AMOUNT RECEIVED", f"${self.__current_transaction_payments_made}"])

        change = self.__current_transaction_payments_made - self.__current_transaction_total

        data.append(["BALANCE GIVEN", f"${change}"])

        table = tabulate(data, headers)

        receipt += table
        print(receipt)

    def __prompt_another_item(self):
        while True:
            response = input("\nWould you like to scan another item? (Y/N): ")
            response = response.strip()

            if response.lower() == "y":
                return True
            if response.lower() == "n":
                return False
            print("Response not recognised. Please try again.")

    def __prompt_barcode(self):
        barcode = input("\nPlease enter the barcode of your item: ")
        self.__scan_item(barcode)

    def __prompt_payment(self):
        print(f"\nPayment due: ${self.__current_transaction_payment_due}")
        payment = input(f"Please enter an amount to pay: ")
        if self.__is_valid_payment(payment):
            # Convert to decimal with 2 decimal places then pass to accept payment
            payment = Decimal(payment)
            payment = payment.quantize(Decimal("0.00"))
            self.accept_payment(Decimal(payment))
        else:
            self.__show_error_invalid_payment_amount()

    def __save_transaction(self, date, barcode, amount):
        pass

    # scan item from input barcode
    def __scan_item(self, barcode):
        barcode = barcode.strip()

        # If invalid input, exit
        if not self.__is_valid_barcode(barcode):
            CheckoutRegister.__show_error_barcode()
            return

        # get product, add to transaction list and total
        product = self.__get_product(barcode)
        self.__current_transaction_list.append(product)
        self.__current_transaction_total += product.get_price()
        self.__current_transaction_payment_due += product.get_price()

        # build output string and display
        output = f"ITEM: {product.get_name()}"
        output += f" | PRICE: ${product.get_price()}"
        output += f" | SUBTOTAL: ${self.__current_transaction_total}"
        print(output)

    @staticmethod
    def __show_error_barcode():
        print("ERROR!! Scanned barcode is incorrect")

    @staticmethod
    def __show_error_invalid_payment_amount():
        print("ERROR!! Invalid amount entered. Please try again.")

    def start(self):
        print("\n\nWelcome to the Self Service Checkout.")

        # Scan items
        continue_scan = True
        while continue_scan:
            self.__prompt_barcode()
            continue_scan = self.__prompt_another_item()

        # Accept payments
        continue_pay = True
        while continue_pay:
            self.__prompt_payment()
            continue_pay = self.__is_payment_complete()

        # Save transaction

        self.__print_receipt()

        # Prompt new customer


