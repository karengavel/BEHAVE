import string
import time

from appium.webdriver.common.touch_action import TouchAction
from behave import *
from screens.products.product_screens import ProductScreen
from utils.dictionaries.product_screen_text import PRODUCT_TEXT


@Then('we see the Products price "{price}"')
def step_impl(context, price):
    product_screen = ProductScreen(context)
    product_screen.assert_text(*product_screen.lbl_price_product, text=price)


@Then('we see the Products name "{name}"')
def step_impl(context, name):
    product_screen = ProductScreen(context)
    product_screen.assert_text(*product_screen.lbl_name_product, text=name)


@When("we tap on the Cart")
def step_impl(context):
    product_screen = ProductScreen(context)
    product_screen.tap_element(*product_screen.btn_cart)


@When("we tap on Add To Cart")
def step_impl(context):
    product_screen = ProductScreen(context)
    product_screen.tap_element(*product_screen.btn_add_cart)


@When("we see a number one on the Cart")
def step_impl(context):
    product_screen = ProductScreen(context)
    product_screen.assert_text(*product_screen.lbl_number_cart, text=PRODUCT_TEXT.get('lbl_number_cart'))


@Then('we see the products in asc order')
def step_impl(context):
    product_screen = ProductScreen(context)
    first_product = product_screen.find_element(*product_screen.lbl_price_first_product).text
    product_screen.driver.swipe(150, 400, 150, -800, 1000)
    last_product = product_screen.find_element(*product_screen.lbl_price_last_product).text
    fp_noprice_convert = first_product.replace('$', '')
    lp_noprice_convert = last_product.replace('$', '')
    compare_price_asc = float(fp_noprice_convert) < float(lp_noprice_convert)
    assert compare_price_asc
