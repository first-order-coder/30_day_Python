from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

PATH = 'C:\Program Files (x86)\chromedriver.exe'

driver = webdriver.Chrome(PATH)
driver.get('https://www.daraz.lk/#')
print(driver.title)

# To insert item into search bar we use this
search = driver.find_element('id',"q")
search.send_keys('a13')
search.send_keys(Keys.RETURN)

html = driver.find_element(By.TAG_NAME, 'html')
html.send_keys(Keys.END)

time.sleep(10)


main = driver.find_element(By.CLASS_NAME ,"box--ujueT")

with open(r'C:\Users\ginuram\Desktop\Dekstop\30DaysofPython\phone.text', 'a') as f:
    f.write(main.text)

# To click and go to next page we use this code
link = driver.find_element(By.LINK_TEXT, 'Samsung Galaxy A13')
link.click()

capacity = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.LINK_TEXT, 'Visit Store')))
capacity.click()

addtocart = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID, "module_add_to_cart")))
addtocart.click()

go_to_cart = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CLASS_NAME, "next-btn next-btn-secondary next-btn-large checkout-order-total-button automation-checkout-order-total-button-cartButton")))
go_to_cart.click()
google = WebDriverWait(driver,10).until(EC.presence_of_element_located(((By.CSS_SELECTOR, "button.mod-button mod-button mod-third-party-login-btn mod-third-party-login-google"))))
google.click()

quantity = driver.find_element(By.LINK_TEXT, '+')
quantity.click()

