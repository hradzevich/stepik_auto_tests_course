from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select


link = "http://suninjuly.github.io/selects1.html"

try:
    # Открываем страницу
    browser = webdriver.Chrome()
    browser.get(link)

    # Находим на странице элемент содержащий первое значение
    value1_element = browser.find_element(By.ID, "num1")

    # Атрибут text возвращает текст, который находится между открывающим и закрывающим тегами элемента, то есть нужно значение
    value1 = value1_element.text

    # Находим на странице элемент содержащий второе значение
    value2_element = browser.find_element(By.ID, "num2")

    # Атрибут text возвращает текст, который находится между открывающим и закрывающим тегами элемента, то есть нужно значение
    value2 = value2_element.text

    # Находим сумму значений
    total = int(value1) + int(value2)

    # Инициализируем новый объект класса Select с элементом с id = "dropdown"
    select = Select(browser.find_element(By.ID, "dropdown"))

    # Ищем нужный нам вариант по видимому тексту
    select.select_by_visible_text(str(total))

    # Нажимаем на кнопку Submit
    submit_btn = browser.find_element(By.CSS_SELECTOR, 'button.btn[type="submit"]')
    submit_btn.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()
