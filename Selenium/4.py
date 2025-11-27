from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time


PATH = 'C:\Program Files (x86)\chromedriver.exe'
driver = webdriver.Chrome(PATH)
driver.get('https://www.daraz.lk/')
driver.maximize_window()

search = driver.find_element(By.ID, "q")
search.send_keys('apple')
search.send_keys(Keys.RETURN)

apple = driver.find_element(By.LINK_TEXT, 'Apple iPhone 14 Pro Max')
apple.click()

size = driver.find_element(By.CSS_SELECTOR, "span.sku-variable-name-text")
size.click()

quantitiy = driver.find_element(By.CSS_SELECTOR, "i.next-icon.next-icon-add.next-icon-medium")
quantitiy.click()

# quantitiy1 = driver.find_element(By.CSS_SELECTOR, "span.next-input.next-input-single.next-input-medium.next-number-picker-input")
# quantitiy1.send_keys('2')

# cart =  driver.find_element(By.CSS_SELECTOR,  "button.ncss-btn-primary-dark.btn-lg.add-to-cart-btn")
# cart.click()
time.sleep(30)

check_out = driver.find_element(By.LINK_TEXT, "Buy Now")
check_out.click()

# name = driver.find_element(By.ID, "firstName")
# name.send_keys('Ginura')

# lst_name =  driver.find_element(By.ID, "lastName" )
# lst_name.send_keys('Amarasena')

# manual_address = driver.find_element(By.ID, "addressSuggestionOptOut")
# manual_address.click()

# time.sleep(3)

# address_1 = driver.find_element(By.ID, "address1")
# address_1.send_keys('108 S A Rd')

# address_2 = driver.find_element(By.ID, "city")
# address_2.send_keys('Trumbull')

# zip = driver.find_element(By.ID, "postalcode")
# zip.send_keys('68980-1720')

# email = driver.find_element(By.ID, 'email')
# email.send_keys('')

# ph = driver.find_element(By.ID, 'phoneNumber')
# ph.send_keys('')

# pay = driver.find_element(By.CLASS_NAME, "gl-cta .gl-cta--primary.gl-cta--full-width")
# pay.click()


# shoes = driver.find_element(By.LINK_TEXT, 'shoes')
# shoes.click()


# login = driver.find_element(By.CLASS_NAME, "gl-cta__content")
# login.click()

# driver.implicitly_wait(10)

# email = driver.find_element(By.ID, "login-register-auto-flow-input")
# email.send_keys('')

# driver.implicitly_wait(10)

# conti = driver.find_element(By.CLASS_NAME, "gl-cta.gl-cta--full-width.gl-cta--icon")
# conti.click()

# faecbook_email = driver.find_element(By.ID, "email")
# faecbook_pass = driver.find_element(By.ID, "pass")
# faecbook_email.send_keys('')
# faecbook_pass.send_keys('')
# faecbook_email.send_keys(Keys.RETURN)
# faecbook_pass.send_keys(Keys.RETURN)


time.sleep(20)