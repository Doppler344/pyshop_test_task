import scrapy

from scrapy_selenium import SeleniumRequest, SeleniumMiddleware

from ozon_top_100.items import OzonTop100Item

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
import undetected_chromedriver


class OzonSpiderSpider(scrapy.Spider):
    name = 'ozon_spider'
    # allowed_domains = ['ozon']
    domain = 'https://www.ozon.ru'
    url = 'https://www.ozon.ru/category/smartfony-15502/?sorting=rating'
    amount_of_pages = 3
    item_list = []
    item_dict = dict()
    def start_requests(self):
        options = undetected_chromedriver.ChromeOptions()
        options.add_argument("--disable-blink-features=AutomationControlled")
        s = Service(
            executable_path="C:\\Users\\Doppl\\PycharmProjects\\pyshop_test\\parse\\chromedriver\\chromedriver2.exe")

        driver = undetected_chromedriver.Chrome(service=s, options=options)
        driver.get(self.url)
        for _ in range(self.amount_of_pages):
            try:
                time.sleep(5)

                link_el = driver.find_elements(By.CSS_SELECTOR, 'a[class="tile-hover-target k8n"]')
                for val in link_el:
                    print('CHECK', )
                    self.item_list.append(val.get_attribute('href'))

                btn = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[4]/div[2]/div/div[1]/div[2]/a/div/div')
                btn.click()
            except Exception as ex:
                print(ex)

        driver.close()
        driver.quit()

        for i in self.item_list[:3]:
            print('CHECK', i)
            yield SeleniumRequest(url=i, wait_time=10, wait_until=EC.element_to_be_clickable((By.XPATH,
                                                                                                 '/html/body/div[1]/div/div[1]/div[5]/div/div[1]/div[3]/div[2]/div[1]/div/div[3]/div/div[1]/div/div/div/div/button/span/span')),
                              callback=self.parse)

    def parse(self, response: scrapy.http.Response):
        title = response.css('h1 ::text').get()
        # for atr, val in zip(response.css('dl.x3l/*/span.l3x ::text'), response.css('dl.x3l/dd.lx3 ::text')):
        #     os = atr.get()
        #     if os.find('Операционная система') > -1:
        #         self.item_dict[title] = val.get()
        #         item = OzonTop100Item()
        #         item['title'] = title
        #         item['atr'] = os
        #         item['os'] = val.get()
        #         yield item

        for pack in response.css('dl.x3l ::text'):
            os = pack.get()
            if os.find('Операционная система') > -1:
                # self.item_dict[title] = val.get()
                item = OzonTop100Item()
                item['title'] = title
                item['atr'] = os
                # item['os'] = val.get()
                yield item


        # self.item_dict[title]
        # for val in response.css('a[class="tile-hover-target k8n"] ::attr(href)'):
        #     item = OzonTop100Item()
        #     item['title'] = val.get()
        #     self.item_list.append(item)
        #     yield item

    def close(spider, reason):
        print('SAAAAAAAAAAAAAAAAK')
