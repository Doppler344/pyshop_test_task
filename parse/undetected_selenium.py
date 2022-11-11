
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import undetected_chromedriver

if __name__ == '__main__':
    options = undetected_chromedriver.ChromeOptions()
    options.add_argument("--disable-blink-features=AutomationControlled")

    url = "https://www.ozon.ru/category/smartfony-15502/?sorting=rating"
    url = "https://www.ozon.ru/category/smartfony-15502/?page=2&sorting=rating"
    s = Service(executable_path="C:\\Users\\Doppl\\PycharmProjects\\pyshop_test\\parse\\chromedriver\\chromedriver.exe")

    driver = undetected_chromedriver.Chrome(service=s, options=options)

    xpath = '/html/body/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[4]/div[1]/div/div/div[*]/div[2]/div/a'
    # /html/body/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[4]/div[1]/div/div/div[2]/div[2]/div/a
    # /html/body/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[4]/div[1]/div/div/div[27]/div[2]/div/a

    try:
        driver.get(url)

        time.sleep(3)
        link_el = driver.find_elements(By.XPATH, xpath)
        x = link_el[0].get_attribute('href')
        print(len(link_el))
        # print(link_el.get_attribute('href'))

        input()
        driver.get(x)
        # time.sleep(5000)

    except Exception as e:
        print(e)
    finally:
        driver.close()
        driver.quit()
