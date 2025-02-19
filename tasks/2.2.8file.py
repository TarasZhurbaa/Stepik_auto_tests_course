from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os 

try:
    link = "https://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    first_name = browser.find_element(By.CSS_SELECTOR, "input[name='firstname']")
    first_name.send_keys("Taras")

    second_name = browser.find_element(By.CSS_SELECTOR, "input[name='lastname']")
    second_name.send_keys("Zhurba")

    email = browser.find_element(By.CSS_SELECTOR, "input[name='email']")
    email.send_keys("email@gmail.com")

    btn_dwnld = browser.find_element(By.ID, "file")

    current_dir = os.path.abspath(os.path.dirname(__file__)) 
    file_path = os.path.join(current_dir, 'file.txt')           
    btn_dwnld.send_keys(file_path)

    btn_submit = browser.find_element(By.CLASS_NAME, "btn")
    btn_submit.click()


finally:
    time.sleep(10)
    browser.quit()    

