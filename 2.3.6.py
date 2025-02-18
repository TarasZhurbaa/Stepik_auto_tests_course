from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element(By.CLASS_NAME, "btn")
    button.click()

    time.sleep(2)
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    
    x = browser.find_element(By.ID, "input_value").text

    input = browser.find_element(By.ID, "answer")
    input.send_keys(calc(x))

    submit = browser.find_element(By.CLASS_NAME, "btn")
    submit.click()

finally:
    time.sleep(10)
    browser.quit()