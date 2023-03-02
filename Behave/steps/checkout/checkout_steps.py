from behave import *
from screens.checkout.checkout_screens import CheckOutScreen


@When('we enter the full name')
def step_impl(context):
    chout_screen = CheckOutScreen(context)
    chout_screen.fill_text(*chout_screen.txt_full_name, text="Rebecca Winter")


@When('we enter the address')
def step_impl(context):
    chout_screen = CheckOutScreen(context)
    chout_screen.fill_text(*chout_screen.txt_address, text="Mandorley 112")


@When('we enter the city')
def step_impl(context):
    chout_screen = CheckOutScreen(context)
    chout_screen.fill_text(*chout_screen.txt_city, text="Truro")


@When('we enter the zip code')
def step_impl(context):
    chout_screen = CheckOutScreen(context)
    chout_screen.fill_text(*chout_screen.txt_zip_code, text="89750")


@When('we enter the country')
def step_impl(context):
    chout_screen = CheckOutScreen(context)
    chout_screen.fill_text(*chout_screen.txt_country, text="United Kingdom")


@When('we tap to payment')
def step_impl(context):
    chout_screen = CheckOutScreen(context)
    chout_screen.tap_element(*chout_screen.btn_to_payment)

