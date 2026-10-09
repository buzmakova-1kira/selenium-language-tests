import time
from selenium.webdriver.common.by import By


def test_button_add_to_basket_is_present(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    browser.get(link)

    # Пауза, чтобы визуально проверить, что язык интерфейса применился
    time.sleep(30)

    # Ищем кнопку добавления в корзину. Селектор уникален для этой страницы.
    button = browser.find_element(By.CSS_SELECTOR, 'button.btn-add-to-basket')

    # Проверяем, что кнопка найдена и видима
    assert button.is_displayed(), 'Кнопка добавления в корзину не найдена'