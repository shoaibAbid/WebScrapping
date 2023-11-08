from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys

PATH="C:\Program Files (x86)\chromedriver.exe"
driver=webdriver.Chrome(PATH)



driver.maximize_window()
driver.get("https://en-gb.facebook.com/")
driver.find_element(By.XPATH,"//*[text()='Create New Account']").click()
time.sleep(3)

driver.find_element(By.NAME,"firstname".send_keys("Shoaib"))
driver.find_element(By.NAME,"lastname".send_keys("Abid"))
driver.find_element(By.NAME,"reg_email__".send_keys("shobiuet8888@gmail.com"))
driver.find_element(By.NAME,"reg_email_confirmation".send_keys("shobiuet8888@gmail.com"))
driver.find_element(By.ID,"password_step_input".send_keys("9090909090"))
day=Select(driver.find_element(By.XPATH,"//select[@title='Day']"))
day.select_by_visible_text("25")
month=Select(driver.find_element(By.NAME,"birthday_month"))
day.select_by_visible_text("Dec")
year=Select(driver.find_element(By.NAME,"birthday_year"))
day.select_by_visible_text("1998")
driver.find_element(By.XPATH,"//label[text()='Male']").click()
driver.find_element(By.XPATH,"//button[text()='Sign Up']").click()









