from selenium import webdriver
import time
from fake_useragent import UserAgent

useragent = UserAgent()

# url = "https://www.instagram.com"
# options
options = webdriver.ChromeOptions()
# options.add_argument("user-agent=HelloWorld)")
# options.add_argument(f"user-agent={useragent.opera}")
options.add_argument(f"user-agent={useragent.random}")

# set proxy
options.add_argument("--proxy-server=52.221.227.46:80")

driver = webdriver.Chrome(
    executable_path="C:\\Users\\admin\\Desktop\\PythonTest\\selenium-python\\chromedriver\\chromedriver.exe",
                          options=options
)
# driver = webdriver.Chrome(executable_path=r"C:\Users\admin\Desktop\PythonTest\selenium-python\chromedriver\chromedriver.exe")

try:
    # driver.get(url="http://whatsmyuseragent.org/")
    # time.sleep(5)
    # driver.get_screenshot_as_file("1.png")
    # driver.get(url="https://yandex.ru")
    # time.sleep(5)
    # driver.save_screenshot("2.png")
    # driver.refresh()
    # time.sleep(2)
    driver.get(url="https://2ip.ru/")
    time.sleep(5)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()