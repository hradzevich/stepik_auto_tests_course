from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

link = "http://suninjuly.github.io/file_input.html"

try:
    # Открываем страницу
    browser = webdriver.Chrome()
    browser.get(link)

    # Находим расположение полей ввода и вносим необходимые данные
    input1 = browser.find_element(By.NAME, "firstname")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.NAME, "lastname")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.NAME, "email")
    input3.send_keys("test@test.com")

    # Находим расположение элемента добавления файла
    input4 = browser.find_element(By.ID, "file")

    # Получаем путь к директории текущего исполняемого файла
    current_dir = os.path.abspath(os.path.dirname(__file__))

    # Добавляем к этому пути имя файла
    file_path = os.path.join(current_dir, "file.txt")

    # Загружаем файл
    input4.send_keys(file_path)

    # Находим элемент кнопки на странице
    button = browser.find_element(By.CSS_SELECTOR, 'button.btn[type="submit"]')

    # Нажимаем на кнопку Submit
    button.click()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
