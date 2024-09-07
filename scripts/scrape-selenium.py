from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
import traceback

# 設定 Firefox options
firefox_options = Options()
firefox_options.add_argument("--headless")  # 在無頭模式下運行

# 設定 FirefoxDriver
driver = webdriver.Firefox(service=Service(), options=firefox_options)

url = "https://www.twitch.tv/"

try:
    # 瀏覽目標網站
    driver.get(url)
    
    # print content of the page
    # print(driver.page_source)

    __ = driver.find_elements(By.CSS_SELECTOR, ".Layout-sc-1xcs6mc-0.jxGBqp")[0]
    # print(__)
    
    # print all href in __
    elements = __.find_elements(By.TAG_NAME, "a")  # 找到所有的 <a> 標籤

    hrefs = [element.get_attribute("href") for element in elements]  # 獲取所有的 href
    print(hrefs)  # 輸出所有的 href
    
    with open("links.txt", "w") as file:
        for href in hrefs:
            file.write(href + "\n")


except Exception as e:
    # 捕獲並打印錯誤訊息
    print("出現錯誤: ", e)
    traceback.print_exc()

finally:
    # 關閉瀏覽器
    driver.quit()
