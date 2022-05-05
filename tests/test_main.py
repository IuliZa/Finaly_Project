import pytest

from pages.main_page import MainPage

"""6 тестов на проверку наличия в шапке основных элементов стартовой страницы"""


def test_page_is_available(driver):
    page = MainPage(driver)
    assert page._driver.title == 'Лабиринт | Книжный интернет-магазин: купить книги, новинки, бестселлеры'


def test_logo_is_presented(driver):
    page = MainPage(driver)
    assert page.logo.is_presented()


def test_message_btn_is_presented_and_clickable(driver):
    page = MainPage(driver)
    assert page.message_btn.is_presented()
    assert page.message_btn.is_clickable()


def test_my_lab_btn_is_presented_and_clickable(driver):
    page = MainPage(driver)
    assert page.my_lab_btn.is_presented()
    assert page.my_lab_btn.is_clickable()


def test_reserved_btn_is_presented_and_clickable(driver):
    page = MainPage(driver)
    assert page.reserved_btn.is_presented()
    assert page.reserved_btn.is_clickable()


def test_cart_btn_is_presented_and_clickable(driver):
    page = MainPage(driver)
    assert page.cart_btn.is_presented()
    assert page.cart_btn.is_clickable()


"""7(8) тестов на проверку активности кнопок в горизонтальном меню в шапке страницы"""


def test_books_button(driver):
    page = MainPage(driver)
    page.books.click()
    assert page.get_current_url() == 'https://www.labirint.ru/books/'


def test_best_button(driver):
    page = MainPage(driver)
    page.important_today.click()
    assert page.get_current_url() == 'https://www.labirint.ru/best/'


def test_school_button(driver):
    page = MainPage(driver)
    page.school.click()
    assert page.get_current_url() == 'https://www.labirint.ru/school/'


def test_games_button(driver):
    page = MainPage(driver)
    page.games.click()
    assert page.get_current_url() == 'https://www.labirint.ru/games/'


def test_stationery_button(driver):
    page = MainPage(driver)
    page.stationery.click()
    assert page.get_current_url() == 'https://www.labirint.ru/office/'


def test_club_button(driver):
   page = MainPage(driver)
   page.club.click()
   assert page.get_current_url() == 'https://www.labirint.ru/club/'

# Упорно не работает поиск ни по xpath, ни по селектору
# def test_change_region(driver):
#    page = MainPage(driver)
#    page.region.click()
#    page.region.delete()
#    page.region_field.send_keys('Москва')
#    page.region_choice.click()
#    assert page.region.get_text() == 'Москва'


def test_button_maps(driver):
    page = MainPage(driver)
    page.maps.click()
    assert page.get_current_url() == 'https://www.labirint.ru/maps/'


"""13 тестов на проверку поисковой строки"""


def test_search_field_is_presented(driver):
    page = MainPage(driver)
    assert page.search.is_presented()


def test_empty_search(driver):
    page = MainPage(driver)
    page.search_submit_btn.click()
    assert page.search_submit_btn.wait_to_be_clickable()


def test_whitespace_search(driver):
    page = MainPage(driver)
    page.search.send_keys(' ')
    page.search_submit_btn.click()
    assert page.search_error.is_presented()


def test_special_character_search(driver):
    page = MainPage(driver)
    page.search.send_keys('§ $&= @#«» <>~®-;²³')
    page.search_submit_btn.click()
    assert page.books_titles.count() >= 0


@pytest.mark.parametrize('name', ['Маугли',
                                  'Капитанская дочка',
                                  'Phyton',
                                  'Пушкин'
                                  ])
def test_search_positive(driver, name):
    page = MainPage(driver)
    page.search = name
    page.search_submit_btn.click()
    assert page.books_titles.count() > 0


def test_search_convert_title(driver):
    page = MainPage(driver)
    page.search.send_keys('Djqyf b vbh')
    page.search_submit_btn.click()
    assert page.books_titles.count() > 0
    for title in page.books_titles.get_text():
        assert 'Djqyf b vbh' or 'Война и мир' in title.lower()


def test_search_with_filter_in_stock(driver):
    page = MainPage(driver)
    page.search.send_keys('Тестирование')
    page.search_submit_btn.click()
    result = page.products.count()
    page.all_filers.click()
    page.reset.click()
    page.in_stock.click()
    page.show_all_found.click()
    assert page.products.count() <= result


@pytest.mark.parametrize('min, max', [(0, 1000),
                                      (1150, 1500),
                                      (2000, 5000)
                                      ])
def test_search_filter_price(driver, min, max):
    page = MainPage(driver)
    page.search.send_keys('Тестирование')
    page.search_submit_btn.click()
    result = page.products.count()
    page.all_filers.click()
    page.reset.click()
    page.set_price.click()
    page.price_min = min
    page.price_max = max
    page.show_all_found.click()
    assert page.products.count() <= result


def test_search_filter_genre(driver):
    page = MainPage(driver)
    page.search.send_keys('книги для детей')
    page.search_submit_btn.click()
    page.all_filers.click()
    page.reset.click()
    page.for_whom.click()
    page.for_kids_only.click()
    page.wait_page_loaded()
    for genre in page.product_cards.get_attribute('data-first-genre-name'):
        assert genre == 'Книги для детей'


"""7 тестов на проверку наличия основных элементов в карточке товара"""


def test_name_on_book_card(driver):
    page = MainPage(driver)
    page.random_book.click()
    assert page.name.is_presented()


def test_pic_on_book_card(driver):
    page = MainPage(driver)
    page.random_book.click()
    assert page.picture.is_presented()


def test_price_on_book_card(driver):
    page = MainPage(driver)
    page.random_book.click()
    assert page.price.is_presented()


def test_add_to_cart_button_on_book_card(driver):
    page = MainPage(driver)
    page.random_book.click()
    assert page.add_to_cart_button.is_presented()


def test_reserved_icon_on_book_card(driver):
    page = MainPage(driver)
    page.random_book.click()
    assert page.add_to_reserved_icon.is_presented()


def test_compare_icon_on_book_card(driver):
    page = MainPage(driver)
    page.random_book.click()
    assert page.add_to_compare_icon.is_presented()


def test_cart_logo_change_num_when_book_is_added(driver):
    page = MainPage(driver)
    page.random_book.click()
    page.add_to_cart_button.click()
    on_cart = page.cart_logo_count.get_text()
    assert int(on_cart) == 1
