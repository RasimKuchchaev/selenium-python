from selenium import webdriver
import time
import xlwt
from xlwt import Workbook

# Рабочая книга создана
wb = Workbook()

# add_sheet используется для создания листа.
sheet1 = wb.add_sheet('Avito')

sheet1.write(0, 0, 'URL')
sheet1.write(0, 1, 'USERNAME')
sheet1.write(0, 2, 'Data Obyavleniya')
sheet1.write(0, 3, 'Data registration')

x = 1
y = 0



# options
options = webdriver.ChromeOptions()

options.add_argument("user-agent=Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0")

#WebDriver Control Power
options.add_argument("--disable-blink-features=AutomationControlled")

#headless mode
# options.add_argument("--headless")
# options.headless = True

driver = webdriver.Chrome(
    executable_path="C:\\Users\\admin\\Desktop\\PythonTest\\selenium-python\\chromedriver\\chromedriver.exe",
                          options=options
)


try:
    driver.get(url="https://www.avito.ru/mahachkala/tovary_dlya_kompyutera/komplektuyuschie/videokarty-ASgBAgICAkTGB~pm7gmmZw?cd=1&p=1")
    driver.implicitly_wait(5)  # если код выпольнился за 1 сек он не ждет еще 4 сек

    item = driver.find_elements_by_xpath("//div[@data-marker='item-photo']")

    for ad in item:
        ad.click()
        # print(driver.window_handles)        # доступ ко вкладкам
        # time.sleep(5)                 # ждет ровно 5 сек
        driver.implicitly_wait(5)       # если код выпольнился за 1 сек он не ждет еще 4 сек

        driver.switch_to.window(driver.window_handles[1])       # перемещение по вкладкам
        print(f"Currently URL is: {driver.current_url}")

        # name_user = driver.find_element_by_xpath("//div[@data-marker='seller-info/name']")
        name_user = driver.find_element_by_class_name("seller-info-name")
        print(f"Name user: {name_user.text}")
        data_obyavleniya = driver.find_element_by_class_name("title-info-metadata-item-redesign")
        print(f"Data Obyavleniya in shop: {data_obyavleniya.text}")
        data_registration_user = driver.find_elements_by_class_name("seller-info-value")[1]
        print(f"Data registration user in: {data_registration_user.text}")
        # time.sleep(5)                 # ждет ровно 5 сек
        driver.implicitly_wait(5)  # если код выпольнился за 1 сек он не ждет еще 4 сек

        sheet1.write(x, y, driver.current_url)
        y += 1
        sheet1.write(x, y, name_user.text)
        y += 1
        sheet1.write(x, y, data_obyavleniya.text)
        y += 1
        sheet1.write(x, y, data_registration_user.text)

        x += 1
        y = 0
        wb.save('example.xls')
        driver.implicitly_wait(5)

        driver.close()
        driver.switch_to.window(driver.window_handles[0])  # перемещение по вкладкам
        print("#" * 20)
        # time.sleep(5)                 # ждет ровно 5 сек
        driver.implicitly_wait(5)  # если код выпольнился за 1 сек он не ждет еще 4 сек

except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()