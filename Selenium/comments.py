from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains

option = Options()

option.add_argument("--disable-infobars")
option.add_argument("--disable-notifications")
option.add_argument("start-maximized")

driver = webdriver.Chrome()
driver.get('https://www.facebook.com/photo/?fbid=724565655705573&set=a.646926206802852')

time.sleep(5)

name = driver.find_element(By.NAME, 'email')
name.send_keys('')

password = driver.find_element(By.NAME, 'pass')
password.send_keys('')

login = driver.find_element(By.CSS_SELECTOR, 'div.x1i10hfl.x1qjc9v5.xjqpnuy.xa49m3k.xqeqjp1.x2hbi6w.x13fuv20.xu3j5b3.x1q0q8m5.x26u7qi.x972fbf.xcfux6l.x1qhh985.xm0m39n.x9f619.x1ypdohk.xdl72j9.x2lah0s.xe8uvvx.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.x2lwn1j.xeuugli.x1n2onr6.x16tdsg8.x1hl2dhg.xggy1nq.x1ja2u2z.x1t137rt.x3nfvp2.x1q0g3np.x87ps6o.x1lku1pv.x1a2a7pz.xtvsq51.xhk9q7s.x1otrzb0.x1i1ezom.x1o6z2jb.x1vqgdyp.x6ikm8r.x10wlt62.xexx8yu.xn6708d.x1120s5i.x1ye3gou')
login.click()

time.sleep(15)

more_comments = driver.find_element(By.XPATH, "//span[contains(text(),'View 32 more comments')]").click()

action = ActionChains(driver)
action.key_down(Keys.END).perform()
action.key_down(Keys.END).perform()
action.key_down(Keys.END).perform()
action.key_down(Keys.END).perform()

time.sleep(10)

names = driver.find_elements(By.XPATH, "//div//span[@class='x3nfvp2']")
comments = driver.find_elements(By.XPATH, "//div//div[@class='x1lliihq xjkvuk6 x1iorvi4']")

for name in names:
    print(name.text)

for comment in comments:
    print(comment.text)
    print("-----------------------")



