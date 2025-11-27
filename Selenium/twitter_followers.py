from selenium import webdriver
from selenium.webdriver import chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

option = Options()
option.add_argument("start-maximized")
option.add_argument("--disable-notifications")

driver = webdriver.Chrome()
driver.get("https://twitter.com/")

time.sleep(15)
login = driver.find_element(By.XPATH, "//span[contains(text(),'Log in')]").click()
time.sleep(3)

username = driver.find_element(By.XPATH, "//input[@name='text']")
username.send_keys("", Keys.ENTER)
time.sleep(3)

password = driver.find_element(By.XPATH, "//input[@name='password']")
password.send_keys("", Keys.ENTER)
time.sleep(3)

search = driver.find_element(By.XPATH, "//a[@aria-label='Search and explore']//div[@class='css-1dbjc4n']//*[name()='svg']").click()
time.sleep(3)

search_item = driver.find_element(By.XPATH, "//input[@placeholder='Search Twitter']")
search_item.send_keys("Elon Musk", Keys.ENTER)

time.sleep(3)

profile = driver.find_element(By.XPATH, "//a[@role='link']//div[@class='css-1dbjc4n r-1awozwy r-18u37iz r-dnmrzs']//div[@class='css-901oao r-1awozwy r-1nao33i r-6koalj r-37j5jr r-a023e6 r-b88u0q r-rjixqe r-bcqeeo r-1udh08x r-3s2u2q r-qvutc0']//span[@class='css-901oao css-16my406 r-poiln3 r-bcqeeo r-qvutc0'][normalize-space()='Elon Musk']").click()
time.sleep(3)

followers = driver.find_element(By.CSS_SELECTOR, "body > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > main:nth-child(4) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(4) > div:nth-child(2) > a:nth-child(1) > span:nth-child(1) > span:nth-child(1)").click()

time.sleep(5)

action = ActionChains(driver)
time_out = time.time() + 10
while time.time() < time_out:
    action.key_down(Keys.END).perform()

time.sleep(100)
infos = driver.find_elements(By.XPATH, "//div[@aria-label='Timeline: Followers']")
for info in infos:
    print(info.text)

action = ActionChains(driver)
time_out = time.time() + 10
while time.time() < time_out:
    action.key_down(Keys.END).perform()