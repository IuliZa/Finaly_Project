import time

import pytest

from pages.cart_page import CartPage
from pages.main_page import MainPage

"""4 теста корзины"""
def test_selected_book_in_cart(driver):
    page = MainPage(driver)
    page.random_book.click()
    page.add_to_cart_button.click()
    page = CartPage(driver)
    assert page.products_in_cart.get_text() == '1 товар'


def test_quantity_buttons(driver):
    page = MainPage(driver)
    page.random_book.click()
    page.add_to_cart_button.click()
    page = CartPage(driver)
    counter = int(page.quantity.get_attribute('value'))
    page.plus_one_more.click()
    time.sleep(10)
    page.minus_one_less.click()
    time.sleep(10)
    assert counter == 1


def test_total_will_change_after_adding_one_more_book(driver):
    page = MainPage(driver)
    page.random_book.click()
    page.add_to_cart_button.click()
    page = CartPage(driver)
    total = int(page.total_of_cart.get_attribute('data-totalprice'))
    page.plus_one_more.click()
    time.sleep(10)
    page.refresh()
    assert int(page.total_of_cart.get_attribute('data-totalprice')) == total * 2


def test_delete_products_from_cart(driver):
    page = MainPage(driver)
    page.random_book.click()
    page.add_to_cart_button.click()
    page = CartPage(driver)
    page.delete_products_from_cart.click()
    assert page.empty_cart


"""4 теста при оформлении заказа из корзины без авторизации на сайте"""


def test_start_checkout_is_presented(driver):
    page = MainPage(driver)
    page.random_book.click()
    page.add_to_cart_button.click()
    page = CartPage(driver)
    assert page.start_checkout_btn.is_presented()

def test_change_delivery_place(driver):
    page = MainPage(driver)
    page.random_book.click()
    page.add_to_cart_button.click()
    page = CartPage(driver)
    page.cookie_policy_btn.click()
    page.start_checkout_btn.click()
    page.delivery_place_change_btn.click()
    assert page.map.is_presented()
    page.delivery_place_field.send_keys('Санкт-Петербург')
    page.pickup_btn_left.click()
    assert page.pick_point_list.count() >= 0


def test_payment_methods_are_available(driver):
    page = MainPage(driver)
    page.random_book.click()
    page.add_to_cart_button.click()
    page = CartPage(driver)
    page.cookie_policy_btn.click()
    page.start_checkout_btn.click()
    assert page.payment_type.is_presented()


def test_checkout_btn_is_presented(driver):
    page = MainPage(driver)
    page.random_book.click()
    page.add_to_cart_button.click()
    page = CartPage(driver)
    assert page.checkout_btn.is_presented()









