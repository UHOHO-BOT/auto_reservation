from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

def get_page_info(driver):
    page_source = driver.page_source
    soup = BeautifulSoup(page_source, "html.parser")
    return soup

def click_target_element(driver, locator, timeout=10):
    """
    ページ内の指定されたロケータにマッチする要素をクリックする関数
    locatorはXPathやCSSセレクターなどで指定
    """
    element = WebDriverWait(driver, timeout).until(
        EC.element_to_be_clickable((By.XPATH, locator))
    )
    element.click()

def post_login_actions(driver):
    """
    ログイン後の一連の操作を統合する関数
    ページ情報の取得と、目当ての要素をクリックする処理を実行
    """
    # ① ページ情報を取得
    page_info = get_page_info(driver)
    print("ページ情報を取得しました。")

    # ② クリックする目当ての要素のロケータを指定（例：'予約する'ボタン）
    target_locator = "//button[contains(text(), '予約する')]"
    click_target_element(driver, target_locator)
    print("目当ての場所をクリックしました。")
