import time
from behave import *
from screens.checkout.checkout_payment_screens import CheckOutPaymentScreen


@When('we enter the buyer full name')
def step_impl(context):
    time.sleep(2.4)
    chout_screen = CheckOutPaymentScreen(context)
    chout_screen.fill_text(*chout_screen.txt_full_name, text="Rebecca Winter")


@When('we enter the card number')
def step_impl(context):
    chout_screen = CheckOutPaymentScreen(context)
    chout_screen.fill_text(*chout_screen.txt_card_number, text="3258 1265 7568 789")


@When('we enter the expiration date')
def step_impl(context):
    chout_screen = CheckOutPaymentScreen(context)
    chout_screen.fill_text(*chout_screen.txt_expiration_date, text="03/25")


@When('we enter the security code')
def step_impl(context):
    chout_screen = CheckOutPaymentScreen(context)
    chout_screen.fill_text(*chout_screen.txt_security_code, text="123")


@When('we tap on review order')
def step_impl(context):
    chout_screen = CheckOutPaymentScreen(context)
    chout_screen.tap_element(*chout_screen.btn_review_order)



