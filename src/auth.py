##########################################################################
## Created on Mar.25th,2025  modified on xxxx
## S.Morita
##ファイルの中からID,パスを取得し、ログイン画面に入力し、ログインボタンを押す。

##手順1
##https://www.shisetsu.city.yokohama.lg.jp/user/Loginに入る

##手順2
##"passid.txt"の中からID,パスをhamaid,hamapassそれぞれに格納する。

##手順3
##ログイン画面のフォームにID,パスを出力する

##手順4
##ログインボタンを押す

##########################################################################


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# ChromeDriverのパスを設定
driver_path = r'C:\Users\sakuras\pystudy\auto_reservation\src\chromedriver-win64\chromedriver-win64\chromedriver.exe'

# Serviceオブジェクトを作成
service = Service(driver_path)

# WebDriverを初期化
driver = webdriver.Chrome(service=service)


# auth.txtからIDとパスワードを読み込む
with open('passid.txt', 'r') as file:
    lines = file.readlines()
    hamaid = lines[0].strip()
    hamapass = lines[1].strip()

# ブラウザを開く
driver = webdriver.Chrome(service=service)


try:
     # 手順1: ログインページにアクセス
    driver.get('https://www.shisetsu.city.yokohama.lg.jp/user/Login')

    # 手順2, 3: フォームにIDとパスワードを入力
    id_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, 'UserLoginInputModel.Id'))
    )
    pass_field = driver.find_element(By.NAME, 'UserLoginInputModel.Password')

    id_field.send_keys(hamaid)
    pass_field.send_keys(hamapass)

    # 手順4: ログインボタンを押す
    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/form/div[2]/ul/li[1]/button'))
    )
    login_button.click()

    time.sleep(10)



finally:
    # Do nothing to keep the browser open
    pass