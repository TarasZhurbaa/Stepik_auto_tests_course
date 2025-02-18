from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "https://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    img = browser.find_element(By.ID, "treasure")
    valuex = img.get_attribute("valuex")
    print(valuex)

    result = calc(valuex)

    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(result)

    checkbox = browser.find_element(By.ID, "robotCheckbox")
    checkbox.click()

    radio = browser.find_element(By.ID, "robotsRule")
    radio.click()

    btn = browser.find_element(By.CSS_SELECTOR, "button.btn")
    btn.click()

finally:
    time.sleep(20)
    browser.quit()   
