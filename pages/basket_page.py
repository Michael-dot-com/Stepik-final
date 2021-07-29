from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_no_product_in_basket(self):
        self.should_be_basket_url()
        self.should_be_basket_is_empty()
        self.should_be_message_that_basket_is_empty()
        self.should_be_valid_empty_massage()

    def should_be_basket_url(self):
        assert "basket" in self.browser.current_url, '"basket" not in current url'

    def should_be_basket_is_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEM), "Basket is not empty, but should be empty"

    def should_be_message_that_basket_is_empty(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_EMPTY_TEXT), \
            "there is no text about an empty basket, should be"

    def should_be_valid_empty_massage(self):
        empty_message = self.browser.find_element(*BasketPageLocators.BASKET_EMPTY_TEXT)
        empty_text = empty_message.text
        assert "is empty" in empty_text, "text not include 'is empty'"
