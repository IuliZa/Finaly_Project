from pages.main_page import WebPage
from pages.elements import WebElement


class ContactPage(WebPage):

    def __init__(self, driver, url=''):
        if not url:
            url = 'https://www.labirint.ru/contact/'

        super().__init__(driver, url)


    call_with_operator = WebElement(xpath='//div[@id="_support_call_number"]/a[@title="Соединить с оператором"]')
    phone_number = WebElement(xpath='//a[contains(text(), "8 800 600-95-25")]')
    e_mail = WebElement(xpath='//a[contains(text(), "shop@labirintmail.ru")]')