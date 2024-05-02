from selenium import webdriver
from selenium.webdriver import chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import pandas as pd

option = Options()
option.add_argument("start-maximized")
option.add_argument("--disable-notifications")

driver = webdriver.Chrome()
driver.get("https://www.youtube.com")

time.sleep(2)
button = driver.find_element(By.CSS_SELECTOR, "button.yt-spec-button-shape-next.yt-spec-button-shape-next--filled.yt-spec-button-shape-next--mono.yt-spec-button-shape-next--size-m").click()
time.sleep(2)

button_corner = driver.find_element(By.XPATH, "//div[@id='start']//button[@id='button']//div").click()
time.sleep(1)

trending = driver.find_element(By.XPATH, "//yt-formatted-string[normalize-space()='Trending']").click()
time.sleep(2)

action = ActionChains(driver)
time_out = time.time() + 3
while time.time() < time_out:
    action.key_down(Keys.END).perform()

from openpyxl import Workbook, load_workbook

wb = Workbook()
ws = wb.active
ws.title = 'Data'

videos = driver.find_elements(By.CLASS_NAME, "style-scope ytd-expanded-shelf-contents-renderer")
title = driver.find_elements(By.ID, "video-title")
channel_name = driver.find_elements(By.CSS_SELECTOR, "a.yt-simple-endpoint.style-scope.yt-formatted-string")


for ch_name in channel_name:
    chn = ch_name.text.strip()
    # ws.append([chn])
    print(f'Channel_Name: {chn}')
for i in title:
    Title = i.text
    #ws.append([Title])
    print(f'Title: {Title}')

wb.save('Data.xlsx')
