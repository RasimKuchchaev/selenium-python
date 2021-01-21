from selenium import webdriver
import time


# url = "https://www.instagram.com"
# options
options = webdriver.ChromeOptions()
options.add_argument("user-agent=HelloWorld)")

driver = webdriver.Chrome(
    executable_path="C:\\Users\\admin\\Desktop\\PythonTest\\selenium-python\\chromedriver\\chromedriver.exe",
                          options=options
)
# driver = webdriver.Chrome(executable_path=r"C:\Users\admin\Desktop\PythonTest\selenium-python\chromedriver\chromedriver.exe")

try:
    driver.get(url="http://whatsmyuseragent.org/")
    time.sleep(5)
    # driver.get_screenshot_as_file("1.png")
    # driver.get(url="https://yandex.ru")
    # time.sleep(5)
    # driver.save_screenshot("2.png")
    # driver.refresh()
    # time.sleep(2)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()