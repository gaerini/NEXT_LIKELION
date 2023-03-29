from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import csv
from selenium.webdriver.common.action_chains import ActionChains

chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

chrome_driver = '.chromedriver'
driver = webdriver.Chrome(chrome_driver, options= chrome_options)

driver.get("https://movie.naver.com")

file = open('naver_top20.csv', mode='w', newline='')
writer = csv.writer(file)
writer.writerow(['rank', 'title', 'outline', 'grade'])

rank_btn = driver.find_element(By.XPATH, '//*[@id="scrollbar"]/div[1]/div/div/ul/li[3]/a')
rank_btn.click()
time.sleep(1)
rank = 1
for i in range(21):
    try:
        rank_i = driver.find_element(By.XPATH, f'/html/body/div/div[4]/div/div/div/div/div[1]/table/tbody/tr[{i+2}]/td[2]/div/a')
        rank_i.click()
        time.sleep(3)

        title = driver.find_element(By.XPATH, '//*[@id="content"]/div[1]/div[2]/div[1]/h3/a[1]').text
        outline = driver.find_element(By.XPATH, '//*[@id="content"]/div[1]/div[2]/div[1]/dl/dd[1]/p/span[1]').text
        director = driver.find_element(By.XPATH, '//*[@id="content"]/div[1]/div[2]/div[1]/dl/dd[2]/p/a').text
        try:
            score = driver.find_element(By.XPATH, '//*[@id="actualPointPersentBasic"]/div/span').text
            pure_score = float(score[7:11])
            writer.writerow([rank, title, outline, pure_score])
        except:
            pure_score = "NULL"
            writer.writerow([rank, title, outline, pure_score])
        
        driver.back()
        time.sleep(1)
        rank += 1
        
    except:
        continue

file.close()

# /html/body/div/div[4]/div/div/div/div/div[1]/table/tbody/tr[11]/td[2]/div/a
# /html/body/div/div[4]/div/div/div/div/div[1]/table/tbody/tr[13]/td[2]/div/a
# /html/body/div/div[4]/div/div/div/div/div[1]/table/tbody/tr[14]/td[2]/div/a
# /html/body/div/div[4]/div/div/div/div/div[1]/table/tbody/tr[22]/td[2]/div/a