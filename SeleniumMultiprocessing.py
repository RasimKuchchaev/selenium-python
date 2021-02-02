from selenium import webdriver
import time
from multiprocessing import Pool


# options
options = webdriver.ChromeOptions()

options.add_argument("user-agent=Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0")

# WebDriver Control Power
options.add_argument("--disable-blink-features=AutomationControlled")

url_list = ["https://yandex.ru", "https://vk.com","https://instagram.com"]


def get_data(url):
    try:
        driver = webdriver.Chrome(
            executable_path="C:\\Users\\admin\\Desktop\\PythonTest\\selenium-python\\chromedriver\\chromedriver.exe",
            options=options
        )
        driver.get(url=url)
        time.sleep(5)
        driver.get_screenshot_as_file(f"media/{url.split('//')[1]}.png")
    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()


if __name__ == '__main__':
    p = Pool(processes=2)
    p.map(get_data, url_list)