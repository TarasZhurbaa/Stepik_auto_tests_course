from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser.get(link)

    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100")
    )
    button = browser.find_element(By.ID, "book")
    button.click()

    x = browser.find_element(By.ID, "input_value").text

    input = browser.find_element(By.ID, "answer")
    input.send_keys(calc(x))

    submit = browser.find_element(By.ID, "solve")
    #browser.execute_script("return arguments[0].scrollIntoView(true);", submit)
    submit.click()


finally:
    time.sleep(5)
    browser.quit()    