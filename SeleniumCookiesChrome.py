from selenium import webdriver
import time
from fake_useragent import UserAgent
from selenium.webdriver.common.keys import Keys
from data_auth import v_pswrd, v_lgn
import pickle       #Cookies


useragent = UserAgent()
# options
options = webdriver.ChromeOptions()

options.add_argument(f"user-agent={useragent.random}")

driver = webdriver.Chrome(
    executable_path="C:\\Users\\admin\\Desktop\\PythonTest\\selenium-python\\chromedriver\\chromedriver.exe",
                          options=options
)


try:
    # driver.get(url="https://vk.com/")
    # time.sleep(5)
    #
    # email_imput = driver.find_element_by_id('index_email')
    # email_imput.clear()
    # email_imput.send_keys(v_lgn)
    # time.sleep(5)
    #
    # password_input = driver.find_element_by_id('index_pass')
    # password_input.clear()
    # password_input.send_keys(v_pswrd)
    # time.sleep(5)
    # password_input.send_keys(Keys.ENTER)
    # time.sleep(10)
    #
    # new_link = driver.find_element_by_id("l_nwsf")
    # new_link.click()
    # time.sleep(10)
    #
    # #cookies
    # pickle.dump(driver.get_cookies(), open(f"{v_lgn}cookies", "wb"))    # save cookies

    driver.get(url="https://vk.com/")
    time.sleep(5)

    for cookie in pickle.load(open(f"{v_lgn}cookies", "rb")):          # load cookies
        driver.add_cookie(cookie)

    time.sleep(5)
    driver.refresh()
    time.sleep(10)

except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()