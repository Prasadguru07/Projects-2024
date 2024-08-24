from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import credentials
# importing credentials

credentials.username = "guruprasad2903@gmail.com"
credentials.password = "Guruprasad@2003"

driver = webdriver.Firefox()
#navigating with firefox webdriver

driver.maximize_window()
#maximizing window

driver.implicitly_wait(20)
driver.get("https://bageasy.in/")
#navigating to bageasy website

WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="shopify-section-header"]/section/header/div/div/div[2]/div[2]/div/a[2]'))).click()
time.sleep(2)

driver.find_element(By.XPATH, "//*[@id=\"customer[email]\"]").send_keys(credentials.username)
#sending username/email to emailform 

driver.find_element(By.XPATH, "//*[@id=\"customer[password]\"]").send_keys(credentials.password)
#sending password to passwordform

WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="customer_login"]/button'))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="shopify-section-template--16601198985470__main"]/section/div/div[2]/div[2]/div/div[2]/div/div[2]/a'))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="product_form_id_7868841722110_template--16601198952702__main"]/button[1]'))).click()


WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mini-cart"]/div/div[2]/div[2]/div/a'))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="shopify-section-template--16601198887166__main"]/section/div[2]/div/div/div/form/div/div[1]/div/button'))).click()

time.sleep(5)