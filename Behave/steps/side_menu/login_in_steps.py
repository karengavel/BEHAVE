import time

from behave import *
from screens.side_menu.log_in_screen import LogInScreen


@When('we enter the correct user')
def step_impl(context):
    time.sleep(2.4)
    log_in = LogInScreen(context)
    log_in.fill_text(*log_in.txt_username, text='bob@example.com')


@When('we enter the correct password')
def step_impl(context):
    log_in = LogInScreen(context)
    log_in.fill_text(*log_in.txt_password, text="10203040")


@When('tap on the Log In button')
def step_impl(context):
    log_in = LogInScreen(context)
    log_in.tap_element(*log_in.btn_login)
