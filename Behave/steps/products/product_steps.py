from behave import *
from screens.products.product_screens import ProductScreen
from utils.dictionaries.product_screen_text import PRODUCT_TEXT


@Then("We see the Product's price")
def step_impl(context):
    product_screen = ProductScreen(context)
    product_screen.assert_text(*product_screen.lbl_price_product, text=PRODUCT_TEXT.get('lbl_price_product'))


@Then("We see the Product's name")
def step_impl(context):
    product_screen = ProductScreen(context)
    product_screen.assert_text(*product_screen.lbl_name_product, text=PRODUCT_TEXT.get('lbl_name_product'))


@When("We tap on Add To Cart")
def step_impl(context):
    product_screen = ProductScreen(context)
    product_screen.tap_element(*product_screen.btn_cart)


@Then("We see a number one on the Cart")
def step_impl(context):
    product_screen = ProductScreen(context)
    product_screen.assert_text(*product_screen.lbl_number_cart, text=PRODUCT_TEXT.get('lbl_number_cart'))
