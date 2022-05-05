import os

from pages.base_page import WebPage
from pages.elements import WebElement, ManyWebElements


class MainPage(WebPage):

    def __init__(self, driver, url=''):
        if not url:
            url = os.getenv("BASE_URL") or 'https://www.labirint.ru'

        super().__init__(driver, url)

    """Шапка"""
    logo = WebElement(xpath='//span[@class = "b-header-b-logo-e-logo"]')
    message_btn = WebElement(xpath='//a[@class="b-header-b-personal-e-link top-link-main have-dropdown-touchlink top-link-main_notification"]')
    my_lab_btn = WebElement(xpath='//a[@class="b-header-b-personal-e-link top-link-main top-link-main_cabinet  js-b-autofade-wrap"]')
    reserved_btn = WebElement(xpath='//a[@class="b-header-b-personal-e-link top-link-main top-link-main_putorder"]')
    cart_btn = WebElement(xpath='//a[@class="b-header-b-personal-e-link top-link-main analytics-click-js cart-icon-js"]')
    books = WebElement(xpath='//a[@class="b-header-b-menu-e-text" and contains(text(), "Книги")]')
    important_today = WebElement(xpath='//a[@class="b-header-b-menu-e-text" and contains(text(), "Главное")]')
    school = WebElement(xpath='//a[@class="b-header-b-menu-e-text" and contains(text(), "Школа")]')
    games = WebElement(xpath='//a[@class="b-header-b-menu-e-text" and contains(text(), "Игрушки")]')
    stationery = WebElement(xpath='//a[@class="b-header-b-menu-e-text" and contains(text(), "Канцтовары")]')
    club = WebElement(xpath='//a[@class="b-header-b-menu-e-text" and contains(text(), "Клуб")]')
#    region = WebElement(xpath='//*[@id="minwidth"]/div[5]/div/div[1]/div[4]/div/div[1]/ul/li[12]/span[1]/span/span[3]/span')
#    region_field = WebElement(xpath='//*[@id="region-post"]')
#    region_choice = WebElement(xpath='//*[@id="ui-id-5"]/a')
    maps = WebElement(xpath='//*[@id="minwidth"]/div[5]/div/div[1]/div[4]/div/div[1]/ul/li[12]/span[2]/span[2]/a')

    """Поиск"""
    search = WebElement(id='search-field')
    search_submit_btn = WebElement(xpath='//button[@type="submit"]')
    search_error = WebElement(xpath ='//div[@class="search-error"]/h1')
    books_titles = ManyWebElements(xpath='//*[@class="product need-watch watched"]')
    all_filers = WebElement(xpath='//span[contains(text(), "ВСЕ ФИЛЬТРЫ") and @class="navisort-item__content"]')
    reset = WebElement(xpath='//*[@id="rubric-tab"]/div[2]/div[1]/div/div[2]/div/span[3]')
    in_stock = WebElement(xpath='//*[@id="section-search-form"]/div[2]/div[2]/div[1]/label[1]/span[2]')
    show_all_found = WebElement(xpath='//input[@class="show-goods__button"]')
    products = ManyWebElements(xpath='//div[@class="products-row "]')
    set_price = WebElement(xpath='//div[@class="search-bl openable price-search"]')
    price_min = WebElement(xpath='//input[@name="price_min"]')
    price_max = WebElement(xpath='//input[@name="price_max"]')
    for_whom = WebElement(xpath='//div[@class="search-bl form-blue openable"]')
    for_kids_only = WebElement(xpath='//*[@id="section-search-form"]/div[4]/div[2]/div[2]/label')
    product_cards = ManyWebElements(xpath='//div[@data-title="Все в жанре «Книги»"]//div[@class="product need-watch watched"]')

    """Карточка товара"""
    random_book = WebElement(xpath='//div[@class="card-column card-column_gutter-60 swiper-slide swiper-slide-next"]')
    name = WebElement(xpath='//div[@id="product-title"]')
    picture = WebElement(xpath='//div[@id="product-image"]/img')
    price = WebElement(xpath='//div[@class="buying-pricenew-text"]')
    add_to_cart_button = WebElement(xpath='//*[@class="btn btn-small btn-primary btn-buy"]')
    add_to_reserved_icon = WebElement(xpath='//a[@class="fave"]')
    add_to_compare_icon = WebElement(xpath='//a[@title="Добавить к сравнению"]')
    cart_logo_count = WebElement(xpath='//span[@class="b-header-b-personal-e-icon-count-m-cart basket-in-cart-a"]')

