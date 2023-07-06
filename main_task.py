from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By

service = Service(executable_path="chromedriver.exe")
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

driver.get('https://google.com')

assert 'Google' in driver.title
elm = driver.find_element(By.NAME, 'q')
elm.send_keys('selenide')

elm.send_keys(Keys.RETURN)
time.sleep(1)

firstLink = driver.find_element(By.ID, 'search').find_element(By.TAG_NAME, 'a')
assert 'https://ru.selenide.org/' in firstLink.get_attribute('href')
time.sleep(1)

imagePageLink = driver.find_element(By.CSS_SELECTOR, 'div[role="navigation"] a')
# imagePageLink = imagePage.find_element(By.TAG_NAME, 'a')
imagePageLink.click()
time.sleep(1)

firstImage = driver.find_element(By.CSS_SELECTOR, 'div[role="main"] img')
assert 'Selenide: лаконичные и стабильные UI тесты на Java' in firstImage.get_attribute('alt')
time.sleep(1)

driver.execute_script("window.history.go(-1)")
time.sleep(1)

firstLink = driver.find_element(By.ID, 'search').find_element(By.TAG_NAME, 'a')
assert 'https://ru.selenide.org/' in firstLink.get_attribute('href')
time.sleep(1)

driver.close()

