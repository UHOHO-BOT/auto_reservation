from .page_navigation import setup_driver, click_target_element
import time

# 定数定義
CHROME_DRIVER_PATH = "C:/Users/june7/OneDrive/Programming/Python/Auto_Reservation/chromedriver-win64/chromedriver.exe"
TARGET_URL = "https://www.shisetsu.city.yokohama.lg.jp/user/Home"
FACILITY_TAB_XPATH = "//*[@id='__BVID__253___BV_tab_button__']"

def main():
    # setup_driver関数を用いてWebDriverのセットアップ
    driver = setup_driver(CHROME_DRIVER_PATH, headless=False)
    
    # 対象ページにアクセス
    driver.get(TARGET_URL)
    
    # "施設名から探す" タブをクリック
    click_target_element(driver, FACILITY_TAB_XPATH)
    print("『施設名から探す』タブをクリックしました。")
    
    # 結果確認待ち（Enterキーを押すまでブラウザは閉じない）
    input("結果を確認できたらEnterキーを押してください...")
    
    driver.quit()

if __name__ == "__main__":
    main()