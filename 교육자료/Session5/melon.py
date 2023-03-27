from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import csv
from selenium.webdriver.common.action_chains import ActionChains


# 디버깅 모드 현재 실행중인 창에서 할 수 있는 설정
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

chrome_driver = '.chromedriver'
driver = webdriver.Chrome(chrome_driver, options= chrome_options)

# 실행할 웹페이지 불러오기 (멜론 차트)
driver.get("https://www.melon.com/index.htm")

# 멜론 차트 버튼 클릭
chartbtn = driver.find_element(By.XPATH, '//*[@id="gnb_menu"]/ul[1]/li[1]/a/span[2]')
chartbtn.click()
time.sleep(3)
# 1위곡명 가져오기
# first = driver.find_element(By.XPATH, f'/html/body/div/div[3]/div/div/div[3]/form/div/table/tbody/tr[{i+1}]/td[6]/div/div/div[1]/span/a').text
    
# 1위부터 20위까지 가져오기
# for i in range(20):
#     first = driver.find_element(By.XPATH, f'/html/body/div/div[3]/div/div/div[3]/form/div/table/tbody/tr[{i+1}]/td[6]/div/div/div[1]/span/a').text
#     print(first)
#     time.sleep(3) 

# 스크롤 내리기

# 실시간 급상승 가수 가져오기
# hover = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div[1]/div[2]/div/ol')

# ActionChains(driver).move_to_element(hover).perform()
# time.sleep(3)

# for i in range(10):
#     singer = driver.find_element(By.XPATH, f'/html/body/div[1]/div[2]/div/div[1]/div[2]/div/ol/li[{i+1}]/a').text

#     time.sleep(2)
#     print(singer)


# 곡의 장르 가져오기
# genre_btn = driver.find_element(By.XPATH, f'/html/body/div/div[3]/div/div/div[3]/form/div/table/tbody/tr[2]/td[4]/div/a/span')
# genre_btn.click()
# time.sleep(3)
# genre = driver.find_element(By.XPATH, '//*[@id="conts"]/div[2]/div/div[2]/div[2]/dl/dd[2]').text
# print(genre)

# 좋아하는 가수의 곡명 10개
# search = driver.find_element(By.XPATH, '//*[@id="top_search"]')
# search.send_keys('BTS')


# search_btn = driver.find_element(By.XPATH, '//*[@id="gnb"]/fieldset/button[2]/span')
# search_btn.click()
# time.sleep(4)

# for i in range(10):
#     search_song = driver.find_element(By.XPATH, f'/html/body/div/div[3]/div/div[1]/div[4]/div/form[1]/div/table/tbody/tr[{i+1}]/td[3]/div/div/a[2]').text
#     print(search_song)


# 순위, 곡명, 가수명 가져오기
file = open('melon.csv', mode='w', newline='')
writer = csv.writer(file)
writer.writerow(['rank', 'song', 'singer'])
for i in range(100):
    rank = driver.find_element(By.XPATH, f'/html/body/div/div[3]/div/div/div[3]/form/div/table/tbody/tr[{i+1}]/td[2]/div/span[1]').text
    song = driver.find_element(By.XPATH, f'/html/body/div/div[3]/div/div/div[3]/form/div/table/tbody/tr[{i+1}]/td[6]/div/div/div[1]/span/a').text
    singer = driver.find_element(By.XPATH, f'/html/body/div/div[3]/div/div/div[3]/form/div/table/tbody/tr[{i+1}]/td[6]/div/div/div[2]/a').text
    writer.writerow([rank, song, singer])
file.close()

# csv 파일로 변환