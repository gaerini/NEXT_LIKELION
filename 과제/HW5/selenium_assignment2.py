from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import csv

chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

chrome_driver = '.chromedriver'
driver = webdriver.Chrome(chrome_driver, options= chrome_options)

driver.get("https://movie.naver.com")

file = open('fav_movie.csv', mode='w', newline='')
writer = csv.writer(file)
writer.writerow(['title', 'director', 'score', 'review_count'])

input_box = driver.find_element(By.XPATH, '//*[@id="ipt_tx_srch"]')
input_box.send_keys('신세계')
time.sleep(1)
input_box.send_keys(Keys.ENTER)
time.sleep(2)

fav_movie = driver.find_element(By.XPATH, '//*[@id="old_content"]/ul[2]/li[5]/dl/dt/a')
fav_movie.click()
time.sleep(2)

title = driver.find_element(By.XPATH, '//*[@id="content"]/div[1]/div[2]/div[1]/h3/a').text
director = driver.find_element(By.XPATH, '//*[@id="content"]/div[1]/div[2]/div[1]/dl/dd[2]/p/a').text
driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)

score = driver.find_element(By.XPATH, '//*[@id="content"]/div[1]/div[4]/div[5]/div[2]/div[2]/div[1]/div/div/em').text
review_count = driver.find_element(By.XPATH, '//*[@id="content"]/div[1]/div[4]/div[5]/div[2]/div[3]/strong/em').text

writer.writerow([title, director, score, review_count])

file.close()