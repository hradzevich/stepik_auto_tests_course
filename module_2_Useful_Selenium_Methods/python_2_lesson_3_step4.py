from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


link = "http://suninjuly.github.io/alert_accept.html"

try:
    # Открываем страницу
    browser = webdriver.Chrome()
    browser.get(link)

    # Нажимаем на кнопку I want to go on a magical journey!
    submit_btn = browser.find_element(
        By.CSS_SELECTOR, 'button.btn-primary[type="submit"]'
    )
    submit_btn.click()

    # Переключаемся на модальное окно Are you sure? и выбираем согласиться
    confirm = browser.switch_to.alert
    confirm.accept()

    # Функция для расчета переменной х
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    # Находим на странице значение х
    x_element = browser.find_element(
        By.XPATH, "//span[@class='nowrap' and @id='input_value']"
    )
    # Атрибут text возвращает текст, который находится между открывающим и закрывающим тегами элемента
    x = x_element.text

    # Вызываем функцию calc(x) для рассчета и сохраняем результат в переменную у
    y = calc(x)

    # Находим поле для ввода резульатов рассчета и вводим результат
    input1 = browser.find_element(
        By.XPATH, "//input[@class='form-control' and @id='answer'and @required]"
    )
    input1.send_keys(y)

    # Нажимаем на кнопку Submit
    submit_btn = browser.find_element(By.CSS_SELECTOR, 'button.btn[type="submit"]')
    submit_btn.click()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
