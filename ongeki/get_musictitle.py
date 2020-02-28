from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from getpass import getpass
from bs4 import BeautifulSoup
import time
import json

#id,passの指定
USER = input("idを入力してください")
PASS = getpass("パスワードを入力してください")

url = "https://ongeki-net.com/ongeki-mobile/"


driver = webdriver.Chrome()
driver.get(url)

#操作
driver.find_element_by_name('segaId').send_keys(USER)
element = driver.find_element_by_name('password')
element.send_keys(PASS)
element.send_keys(Keys.ENTER)
time.sleep(1)
#aime選択
driver.implicitly_wait(1)
xpath = driver.find_element_by_xpath(
    "// button/img")
xpath.click()
time.sleep(1)

#レコードボタン押す
driver.find_element_by_xpath("//header/div/a[2]/img").click()
time.sleep(1)

#楽曲別レコード押す
driver.find_element_by_xpath(
    "//div[2]/div/a[4]/img").click()
time.sleep(2)

#master押す
driver.find_element_by_xpath(
    "//button[4]/img").click()
time.sleep(1)
print("HELLO")
#曲名とレベルの取得
soup = BeautifulSoup(driver.page_source, "lxml")
now = 4
music = dict()
print(soup)
for i in range(1000):
    if not soup.select(".basic_btn:nth-child({}) .music_label".format(now)):
        now = now + 1
        continue
    music[soup.select(".basic_btn:nth-child({}) .music_label".format(now))[0].string
          ] = (soup.select(".basic_btn:nth-child({}) .score_level".format(now))[0].string)
    print(soup.select(
        ".basic_btn:nth-child({}) .music_label".format(now))[0].string)
    print(now)
    now = now + 1
with open('./test.json', 'w') as f:
    json.dump(music, f, indent=4, ensure_ascii=False)
