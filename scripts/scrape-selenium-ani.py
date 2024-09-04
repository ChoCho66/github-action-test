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

url = "https://ani.gamer.com.tw"

try:
    # 瀏覽目標網站
    driver.get(url)
    
    # print content of the page
    # print(driver.page_source)

    # 找到所有 class = "anime-name-block" 的元素
    anime_blocks = driver.find_elements(By.CLASS_NAME, "anime-name-block")
    print(anime_blocks[:10])
    
    print()
    print()
    print("-" * 40)  # 分隔線

    # 迭代前10個 anime-name-block 元素
    for index, block in enumerate(anime_blocks[:10]):
        print(f"Anime Block {index + 1}:")

        # 找到該 anime-name-block 中所有 p 元素
        p_elements = block.find_elements(By.TAG_NAME, "p")

        # 打印每個 p 元素的文本
        for p in p_elements:
            print(p.text)

        print("-" * 40)  # 分隔線

except Exception as e:
    # 捕獲並打印錯誤訊息
    print("出現錯誤: ", e)
    traceback.print_exc()

finally:
    # 關閉瀏覽器
    driver.quit()
