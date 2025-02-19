from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "https://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element(By.CLASS_NAME, "btn")
    button.click()

    confirm = browser.switch_to.alert
    confirm.accept()

    x = browser.find_element(By.ID, "input_value").text

    input = browser.find_element(By.ID, "answer")
    input.send_keys(calc(x))

    submit = browser.find_element(By.CLASS_NAME, "btn")
    submit.click()


finally:
    time.sleep(10)
    browser.quit()
        
