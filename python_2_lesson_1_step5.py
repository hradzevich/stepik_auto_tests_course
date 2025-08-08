from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


link = "https://suninjuly.github.io/math.html"

try:
    # Открываем страницу
    browser = webdriver.Chrome()
    browser.get(link)

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

    # Отмечаем checkbox "I'm the robot" кликом по label
    option1 = browser.find_element(By.CSS_SELECTOR, 'label[for="robotCheckbox"]')
    option1.click()

    # Выюираем radiobutton "Robots rule!" кликом по label
    option2 = browser.find_element(By.CSS_SELECTOR, 'label[for="robotsRule"]')
    option2.click()

    # Нажимаем на кнопку Submit
    submit_btn = browser.find_element(By.CSS_SELECTOR, 'button.btn[type="submit"]')
    submit_btn.click()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
