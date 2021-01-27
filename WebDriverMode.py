from selenium import webdriver
import time
from fake_useragent import UserAgent



useragent = UserAgent()
# options
options = webdriver.ChromeOptions()

options.add_argument(f"user-agent={useragent.random}")
options.add_argument("--disable-blink-features=AutomationControlled")   #WebDriver Control Power

driver = webdriver.Chrome(
    executable_path="C:\\Users\\admin\\Desktop\\PythonTest\\selenium-python\\chromedriver\\chromedriver.exe",
                          options=options
)


try:
    driver.get(url="https://intoli.com/blog/not-possible-to-block-chrome-headless/chrome-headless-test.html")
    time.sleep(10)



except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()