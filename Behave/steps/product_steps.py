from behave import *
from screens.products.product_screens import ProductScreen


@Then("We see the Product's price")
def step_impl(context):
    product = ProductScreen(context)
    product.tap_element(*product.price_product)