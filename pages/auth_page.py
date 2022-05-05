from pages.base_page import WebPage
from pages.elements import WebElement, ManyWebElements


class AuthPage(WebPage):

    def __init__(self, driver, url=''):
        if not url:
            url = 'https://www.labirint.ru/cabinet/'

        super().__init__(driver, url)


    """Мой лабиринт"""

    my_lab_btn = WebElement(xpath='//a[@class="b-header-b-personal-e-link top-link-main top-link-main_cabinet  js-b-autofade-wrap"]')
    cabinet_identifier = WebElement(xpath='//span[@class="cabinet-menu__nowrap"]')
    input_field = WebElement(xpath='//input[@value="+7"]')
    submit_btn = WebElement(xpath='//input[@id="g-recap-0-btn"]')
    error_code_msg = WebElement(xpath='//small[contains(text(), "Введенного кода не существует")]')
    error_invalid_symbol_msg = WebElement(xpath='//small[contains(text(), "Нельзя использовать символ « »")]')
    other_login_methods = WebElement(xpath='//a[@class="js-show-soc analytics-click-js"]')
    social_icons = ManyWebElements(xpath='//div[@class="new-auth__auth-social"]')
    logout_btn = WebElement(xpath='//a[@href="/authorization/logout/"]')
    new_authorize = WebElement(xpath='//div[@class="lab-modal-container new-auth js-new-auth js-new-forms new-forms"]')