from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "http://suninjuly.github.io/execute_script.html"

try:
    # Открываем страницу
    browser = webdriver.Chrome()
    browser.get(link)

    # Функция для расчета переменной х
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    time.sleep(2)

    # Находим на странице значение элемент-картинку со значением х
    x_element = browser.find_element(By.ID, "input_value")

    # Атрибут text возвращает текст, который находится между открывающим и закрывающим тегами элемента
    x = x_element.text

    # Вызываем функцию calc(x) для рассчета и сохраняем результат в переменную у
    y = calc(x)

    # Находим поле для ввода резульатов рассчета
    input1 = browser.find_element(By.XPATH, "//input[@id='answer'and @required]")

    # Запускаем JavaScript скрипт для скролла страницы чтобы нужные элементы не перекрывались футером
    browser.execute_script("return arguments[0].scrollIntoView(true);", input1)

    # Вводим результат
    input1.send_keys(y)

    # Отмечаем checkbox "I'm the robot" кликом
    option1 = browser.find_element(By.CSS_SELECTOR, "input#robotCheckbox")
    option1.click()

    # Выбираем radiobutton "Robots rule!" кликом
    option2 = browser.find_element(By.CSS_SELECTOR, "input#robotsRule")
    option2.click()

    # Находим элемент кнопки на странице
    button = browser.find_element(By.CSS_SELECTOR, 'button.btn[type="submit"]')

    # Нажимаем на кнопку Submit
    button.click()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
