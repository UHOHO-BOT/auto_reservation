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

from page_navigation import click_target_element

def passlogin(PASS_PATH): 
    # auth.txtからIDとパスワードを読み込む
    with open(PASS_PATH, 'r') as file:
        lines = file.readlines()
        hamaid = lines[0].strip()
        hamapass = lines[1].strip()
    return hamaid,hamapass

def login (LOGIN_PAGE_PATH,hamaid,hamapass):
     # 手順1: ログインページにアクセス
    driver.get(LOGIN_PAGE_PATH)

    # 手順2, 3: フォームにIDとパスワードを入力
    id_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, 'UserLoginInputModel.Id'))
    )
    pass_field = driver.find_element(By.NAME, 'UserLoginInputModel.Password')

    id_field.send_keys(hamaid)
    pass_field.send_keys(hamapass)

    # 手順4: ログインボタンを押す

    locator = '//*[@id="app"]/form/div[2]/ul/li[1]/button'

    click_target_element(driver, locator, timeout=10)

   # login_button = WebDriverWait(driver, 10).until(
   #     EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/form/div[2]/ul/li[1]/button'))
   # )
   # login_button.click()

    #time.sleep(10)
# ページを開いたままにする
    input("Press Enter to close the browser and exit...")


#finally:
    # Do nothing to keep the browser open
#    pass


# テスト用のコード
if __name__ == "__main__":
    # テスト用データや設定
    PASS_PATH = '.\passid.txt'
    LOGIN_PAGE_PATH = 'https://www.shisetsu.city.yokohama.lg.jp/user/Login'

    # 関数のテスト実行
    hamapass,hamaid=passlogin(PASS_PATH)
    login(LOGIN_PAGE_PATH,hamaid,hamapass)

