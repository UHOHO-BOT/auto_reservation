from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

def setup_driver(chrome_driver_path, headless=False):
    """
    WebDriver のセットアップを行う関数
    :param chrome_driver_path: ChromeDriver の実行可能ファイルのパス
    :param headless: ヘッドレスモードを有効にする場合は True を指定、デフォルトは False
    :return: セットアップ済みの WebDriver インスタンス
    """
    chrome_options = Options()
    if headless:
        chrome_options.add_argument("--headless")
    service = Service(chrome_driver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)
    return driver

def get_page_info(driver):
    page_source = driver.page_source
    soup = BeautifulSoup(page_source, "html.parser")
    return soup

def click_target_element(driver, locator, timeout=10):
    """
    ページ内の指定されたロケータにマッチする要素をクリックする関数
    locator は XPath や CSS セレクターなどで指定
    """
    element = WebDriverWait(driver, timeout).until(
        EC.element_to_be_clickable((By.XPATH, locator))
    )
    element.click()

def post_login_actions(driver):
    """
    ログイン後の一連の操作を統合する関数
    ① ページ情報の取得、② 目当ての要素のクリックを実施
    """
    page_info = get_page_info(driver)
    print("ページ情報を取得しました。")
    target_locator = "//button[contains(text(), '予約する')]"
    click_target_element(driver, target_locator)
    print("目当ての場所をクリックしました。")

def fill_input_field(driver, text, locator):
    """
    指定したフィールドにテキストを入力する汎用関数

    :param driver: Selenium WebDriver のインスタンス
    :param text: 入力するテキスト
    :param locator: 対象フィールドを特定するための XPath または CSS セレクター
    """
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC

    input_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, locator))
    )
    input_element.clear()  # 既存の内容をクリアする
    input_element.send_keys(text)

