# We recommend installing an extension to run python tests.
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from src import page_navigation  

@pytest.fixture
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    service = Service("C:/Users/june7/OneDrive/Programming/Python/Auto_Reservation/chromedriver-win64/chromedriver.exe")
    driver = webdriver.Chrome(service=service, options=chrome_options)
    yield driver
    driver.quit()



def test_get_page_info(driver):
    driver.get("https://www.shisetsu.city.yokohama.lg.jp/user/Login")
    soup = page_navigation.get_page_info(driver)
    # ページタイトルが存在するかをチェック
    assert soup.title.string is not None
    # ページ情報を整形済みHTMLとしてテキストファイルに保存
    with open("page_info.txt", "w", encoding="utf-8") as f:
        f.write(soup.prettify())


# def test_click_target_element(driver):
#     # インラインHTMLを使用して、クリック後に body に属性が付与されるテスト用ページ
#     html_content = """
#     <html>
#       <head>
#         <script>
#           function onClick() {
#             document.body.setAttribute('data-clicked', 'true');
#           }
#         </script>
#       </head>
#       <body>
#         <button onclick="onClick()">予約する</button>
#       </body>
#     </html>
#     """
#     driver.get("data:text/html;charset=utf-8," + html_content)
#     page_navigation.click_target_element(driver, "//button[contains(text(), '予約する')]")
#     # クリック後の効果を確認
#     clicked = driver.execute_script("return document.body.getAttribute('data-clicked');")
#     assert clicked == "true"

# def test_post_login_actions(driver):
#     # インラインHTMLを使用して、post_login_actions によるクリックを確認するテスト用ページ
#     html_content = """
#     <html>
#       <head>
#         <script>
#           function onClick() {
#             document.body.setAttribute('data-post-login', 'clicked');
#           }
#         </script>
#       </head>
#       <body>
#         <div>ログイン後の情報</div>
#         <button onclick="onClick()">予約する</button>
#       </body>
#     </html>
#     """
#     driver.get("data:text/html;charset=utf-8," + html_content)
#     page_navigation.post_login_actions(driver)
#     # クリックされたかどうか、body の属性で検証
#     result = driver.execute_script("return document.body.getAttribute('data-post-login');")
#     assert result == "clicked"
