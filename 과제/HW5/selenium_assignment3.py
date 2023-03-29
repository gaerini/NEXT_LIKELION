from bs4 import BeautifulSoup
import requests as req
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

chrome_driver = '.chromedriver'
driver = webdriver.Chrome(chrome_driver, options= chrome_options)

driver.get("https://www.melon.com/index.htm")
time.sleep(1)

input_box = driver.find_element(By.XPATH, '//*[@id="top_search"]')
input_box.send_keys('BTS')
input_box.send_keys(Keys.ENTER)
time.sleep(2)

#request
url = driver.current_url
header = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'}
res = req.get(url, headers=header)
soup = BeautifulSoup(res.text, 'html.parser')

li_song = soup.find_all(class_='fc_gray')
li_song_text = [e.text for e in li_song]

for _ in li_song_text:
    print(_)
