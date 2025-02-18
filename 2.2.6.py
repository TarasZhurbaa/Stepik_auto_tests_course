from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    link = " https://SunInJuly.github.io/execute_script.html"
    browser.get(link)

    x = browser.find_element(By.ID, "input_value").text

    input = browser.find_element(By.ID, "answer")
    input.send_keys(calc(x))

    browser.execute_script("window.scrollBy(0, 100);")

    chbox = browser.find_element(By.ID, "robotCheckbox")
    chbox.click()

    radiobtn = browser.find_element(By.ID, "robotsRule")
    radiobtn. click()
    
    btn = browser.find_element(By.CLASS_NAME, "btn")
    btn.click()

finally:
    time.sleep(10)
    browser.quit()