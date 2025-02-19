from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    y = calc(x)

    input1 = browser.find_element(By.CSS_SELECTOR, "#answer")
    input1.send_keys(y)

    chekbox = browser.find_element(By.ID, "robotCheckbox")
    chekbox.click()

    radiobtn = browser.find_element(By.ID, "robotsRule")
    radiobtn.click()

    submit = browser.find_element(By.TAG_NAME, "button")
    submit.click()




finally:
    time.sleep(20)
    browser.quit()   
