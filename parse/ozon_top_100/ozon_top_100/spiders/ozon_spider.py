import scrapy

from scrapy_selenium import SeleniumRequest, SeleniumMiddleware

from ozon_top_100.items import OzonTop100Item

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class OzonSpiderSpider(scrapy.Spider):
    name = 'ozon_spider'
    # allowed_domains = ['ozon']
    domain = 'https://www.ozon.ru'
    url = 'https://www.ozon.ru/category/smartfony-15502/?sorting=rating'
    amount_of_pages = 3
    item_list = []

    def start_requests(self):
        yield SeleniumRequest(url=self.url, wait_time=10, wait_until=EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[4]/div[1]/div/div/div[36]/div[2]/div/a/span')), callback=self.parse)

    def parse(self, response: scrapy.http.Response):
        if self.amount_of_pages > 0:
            self.amount_of_pages - 1

        for val in response.css('a[class="tile-hover-target k8n"] ::attr(href)'):
            item = OzonTop100Item()
            item['url'] = val.get()
            self.item_list.append(item)
            yield item

    def close(spider, reason):
        print('SAAAAAAAAAAAAAAAAK')
