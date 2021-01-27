from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from data_auth import v_pswrd, v_lgn


# options
options = webdriver.ChromeOptions()

options.add_argument("user-agent=Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0")

#WebDriver Control Power
options.add_argument("--disable-blink-features=AutomationControlled")

#headless mode
# options.add_argument("--headless")
options.headless = True

driver = webdriver.Chrome(
    executable_path="C:\\Users\\admin\\Desktop\\PythonTest\\selenium-python\\chromedriver\\chromedriver.exe",
                          options=options
)


try:
    driver.get(url="https://vk.com/")
    time.sleep(5)

    print("Auterization...")
    email_imput = driver.find_element_by_id('index_email')
    email_imput.clear()
    email_imput.send_keys(v_lgn)
    time.sleep(5)

    password_input = driver.find_element_by_id('index_pass')
    password_input.clear()
    password_input.send_keys(v_pswrd)
    time.sleep(5)
    password_input.send_keys(Keys.ENTER)
    time.sleep(10)

    print("Profile ...")
    video_link = driver.find_element_by_id("l_pr")
    video_link.click()
    time.sleep(10)

    print("video start...")
    video = driver.find_element_by_class_name("page_post_sized_thumbs").click()
    time.sleep(20)
    print("video stop")



except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()