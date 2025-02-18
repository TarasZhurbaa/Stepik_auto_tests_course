from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


def calc(x, y):
    return int(x) + int(y)

try:
    link = " https://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = browser.find_element(By.ID, "num1").text
    num2 = browser.find_element(By.ID, "num2").text

    result = str(calc(num1, num2))

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_visible_text(result)

    btn = browser.find_element(By.CSS_SELECTOR, "button.btn")
    btn.click()


finally:
    time.sleep(10)
    browser.quit()







