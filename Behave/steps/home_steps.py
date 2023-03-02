import time

from behave import *
from screens.home_screens import HomeScreen
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.action_chains import ActionChains

from utils.dictionaries.home_screen_texts import HOME_TEXT


@Step('We are in the Home Page')
def step_impl(context):
    home_screen = HomeScreen(context)
    home_screen.find_element(*home_screen.lbl_products)


@Then("We see the Products label")
def step_impl(context):
    home_screen = HomeScreen(context)
    home_screen.assert_text(*home_screen.lbl_products, text=HOME_TEXT.get('lbl_products'))


@Given('we tap in the side menu')
def step_impl(context):
    home_screen = HomeScreen(context)
    home_screen.tap_element(*home_screen.menu_side)


@When('we tap on first product')
def step_impl(context):
    home_screen = HomeScreen(context)
    home_screen.tap_element(*home_screen.first_product)


@When('we tap on sort by')
def step_impl(context):
    home_screen = HomeScreen(context)
    home_screen.tap_element(*home_screen.btn_sort)
