from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import traceback

# 設定 Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # 在無頭模式下運行
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# 設定 ChromeDriver
driver = webdriver.Chrome(service=Service(), options=chrome_options)

url = "https://ani.gamer.com.tw"

try:
    # 瀏覽目標網站
    driver.get(url)

    # 假設我們想要找到某個元素
    element = driver.find_element(By.XPATH, "//h1")

    # 打印該元素的文本
    print(element.text)

except Exception as e:
    # 捕獲並打印錯誤訊息
    print("出現錯誤: ", e)
    traceback.print_exc()

finally:
    # 關閉瀏覽器
    driver.quit()
