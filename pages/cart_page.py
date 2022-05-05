from pages.base_page import WebPage
from pages.elements import WebElement, ManyWebElements


class CartPage(WebPage):

    def __init__(self, driver, url=''):
        if not url:
            url = 'https://www.labirint.ru/cart/'

        super().__init__(driver, url)



    """Корзина товаров"""
    products_in_cart = WebElement(xpath='//span[@id="basket-default-prod-count2"]')
    plus_one_more = WebElement(xpath='//span[@class="btn btn-increase btn-increase-cart"]')
    minus_one_less = WebElement(xpath='//span[@class="btn btn-lessen btn-lessen-cart"]')
    delete_products_from_cart = WebElement(xpath='//a[@class="b-link-popup"]')
    empty_cart = WebElement(xpath='//span[contains(text(),"Ваша корзина пуста. Почему?"]')
    total_of_cart = WebElement(xpath='//*[@id="basket-step1-default"]/div[5]')
    quantity = WebElement(xpath='//input[@class="quantity"]')
    cookie_policy_btn = WebElement(xpath='//button[@class="cookie-policy__button js-cookie-policy-agree"]')
    start_checkout_btn = WebElement(xpath='//button[@class="btn btn-primary btn-large fright start-checkout-js"]')
    delivery_place_change_btn = WebElement(xpath='//button[@class="button-link delivery__profiles-change-btn"]')
    delivery_place_field = WebElement(xpath='//input[@id="deliveryAddress"]')
    pickup_btn_left = WebElement(xpath='//div[@class="div-select-text-left-header"]')
    map = WebElement(xpath='//div[@id="map"]')
    pick_point_list = ManyWebElements(xpath='//div[contains(text(), "Ближайшие пункты выдачи:")]')
    payment_type = WebElement(xpath='//div[@class="type-1 relative js-scroll-to payment"]')
    checkout_btn = WebElement(xpath='//div[@class="base-button--content"]')

