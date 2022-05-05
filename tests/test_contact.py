from pages.contact_page import ContactPage

"""3 теста проверки наличия основынх элементов страницы Контакты"""


def test_connect_with_operator_button_is_presented(driver):
    page = ContactPage(driver)
    assert page.call_with_operator.is_presented()


def test_support_phone_number_is_presented(driver):
    page = ContactPage(driver)
    assert page.phone_number.is_presented()


def test_support_email_is_presented(driver):
    page = ContactPage(driver)
    assert page.e_mail.is_presented()