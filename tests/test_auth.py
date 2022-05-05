import time

from pages.auth_page import AuthPage

"""6 тестов авторизации пользователя"""


def test_log_in_with_valid_data(driver):
    page = AuthPage(driver)
    page.input_field.send_keys('BCAE-42BF-9F25')
    page.submit_btn.click()
    page.wait_page_loaded()
    page.my_lab_btn.click()
    assert page.cabinet_identifier.is_presented()


def test_log_in_with_invalid_data(driver):
    page = AuthPage(driver)
    page.input_field.send_keys('DGTU-4H7F-GHJ5')
    page.submit_btn.click()
    assert page.error_code_msg.is_presented()


def test_log_in_without_data(driver):
    page = AuthPage(driver)
    page.input_field.send_keys('')
    assert page.submit_btn.is_clickable() == False


def test_log_in_with_whitespace(driver):
    page = AuthPage(driver)
    page.input_field.send_keys(' ')
    assert page.error_invalid_symbol_msg.is_presented()


def test_log_in_with_socials(driver):
    page = AuthPage(driver)
    page.other_login_methods.click()
    assert page.social_icons.is_presented()
    assert page.social_icons.count() > 0


def test_log_out_after_successfully_log_in(driver):
    page = AuthPage(driver)
    page.input_field.send_keys('BCAE-42BF-9F25')
    page.submit_btn.click()
    time.sleep(10)
    page.my_lab_btn.move_to_show_submenu()
    page.logout_btn.click()
    page.wait_page_loaded()
    assert page.get_current_url() == 'https://www.labirint.ru/' or page.new_authorize.is_presented()
