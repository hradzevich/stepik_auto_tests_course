from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


link = "http://suninjuly.github.io/get_attribute.html"

try:
    # Открываем страницу
    browser = webdriver.Chrome()
    browser.get(link)

    # Функция для расчета переменной х
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    time.sleep(2)

    # Находим на странице значение элемент-картинку со значением х
    x_element = browser.find_element(By.ID, "treasure")

    # Берем у этого элемента значение атрибута valuex, которое является значением x для задачи
    x = int(x_element.get_attribute("valuex"))

    # Вызываем функцию calc(x) для рассчета и сохраняем результат в переменную у
    y = calc(x)

    # Находим поле для ввода резульатов рассчета и вводим результат
    input1 = browser.find_element(By.XPATH, "//input[@id='answer'and @required]")
    input1.send_keys(y)

    # Отмечаем checkbox "I'm the robot" кликом 
    option1 = browser.find_element(By.CSS_SELECTOR, "input#robotCheckbox")
    option1.click()

    # Выюираем radiobutton "Robots rule!" кликом п
    option2 = browser.find_element(By.CSS_SELECTOR, "input#robotsRule")
    option2.click()

    # Нажимаем на кнопку Submit
    submit_btn = browser.find_element(By.CSS_SELECTOR, 'button.btn[type="submit"]')
    submit_btn.click()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
