from appium.webdriver.common.appiumby import AppiumBy as By
from utils.common_actions import CommonActions


class ProductScreen(CommonActions):
    def __init__(self, context):
        super().__init__(context.driver)
        self.price_product = (By.ACCESSIBILITY_ID, "product price")
        self.name_product = (By.XPATH, "//android.view.ViewGroup[@content-desc='container header']/android.widget.TextView")
