from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("http://37.32.4.222/accounts/login/")
username_input = driver.find_element(By.ID,"id_username")
password_input = driver.find_element(By.ID,"id_password")
username_input.send_keys("abc")
password_input.send_keys("Zaq11qaZ")
submit_btn = driver.find_element(By.XPATH,"/html/body/section/form/input[2]")
submit_btn.click()
driver.implicitly_wait(20)
print("test completed!")
driver.close()