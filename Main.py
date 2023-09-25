from CheckoutRegister import CheckoutRegister


class Main:
    checkout = CheckoutRegister()
    checkout.start()

    # Prompt new customer
    another_customer = True
    while another_customer:
        another_customer = checkout.prompt_new_customer()
        if another_customer:
            checkout.start()


main = Main()


