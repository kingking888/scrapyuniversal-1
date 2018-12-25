# import json
# import logging
# import requests
# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
# from scrapy.http import HtmlResponse
# from selenium.common.exceptions import TimeoutException
#
#
# # 代理设置中间件
# class ProxyMiddleware:
#     def __init__(self, proxy_url):
#         self.logger = logging.getLogger(__name__)
#         self.proxy_url = proxy_url
#
#     @classmethod
#     def from_crawler(cls, crawler):
#         # 在settings.py设置PROXY_URL
#         return cls(
#             proxy_url=crawler.settings.get('PROXY_URL')
#         )
#
#     def get_random_proxy(self):
#         try:
#             response = requests.get(self.proxy_url)
#             if response.status_code == 200:
#                 proxy = response.text
#                 return proxy
#         except requests.ConnectionError:
#             return False
#
#     def process_request(self, request, spider):
#         if request.meta.get('retry_times'):
#             proxy = self.get_random_proxy()
#             if proxy:
#                 uri = 'https://{proxy}'.format(proxy=proxy)
#                 self.logger.debug('使用代理 ' + proxy)
#                 request.meta['proxy'] = uri
#
#
# # Cookies设置中间件
# class CookiesMiddleware:
#     def __init__(self, cookies_url):
#         self.logger = logging.getLogger(__name__)
#         self.cookies_url = cookies_url
#
#     @classmethod
#     def from_crawler(cls, crawler):
#         # 在settings.py设置COOKIES_URL
#         return cls(
#             cookies_url=crawler.settings.get('COOKIES_URL')
#         )
#
#     def get_random_cookies(self):
#         try:
#             response = requests.get(self.cookies_url)
#             if response.status_code == 200:
#                 cookies = json.loads(response.text)
#                 return cookies
#         except requests.ConnectionError:
#             return False
#
#     def process_request(self, request, spider):
#         self.logger.debug('正在获取Cookies')
#         cookies = self.get_random_cookies()
#         if cookies:
#             request.cookies = cookies
#             self.logger.debug('使用Cookies ' + json.dumps(cookies))
#
#
# # selenium中间件
# class SeleniumMiddleware:
#     def __init__(self, timeout=None, service_args=[]):
#         self.logger = logging.getLogger(__name__)
#         self.timeout = timeout
#         self.browser = webdriver.PhantomJS(service_args=service_args)
#         self.browser.set_window_size(1400, 700)
#         self.browser.set_page_load_timeout(self.timeout)
#         self.wait = WebDriverWait(self.browser, self.timeout)
#
#     @classmethod
#     def from_crawler(cls, crawler):
#         return cls(timeout=crawler.settings.get('SELENIUM_TIMEOUT'),
#                    service_args=crawler.settings.get('PHANTOMJS_SERVICE_ARGS'))
#
#     def __del__(self):
#         self.browser.close()
#
#     def process_request(self, request, spider):
#         """
#         用PhantomJS抓取页面
#         :return: HtmlResponse
#         """
#         self.logger.debug('PhantomJS is Starting')
#         page = request.meta.get('page', 1)
#         try:
#             self.browser.get(request.url)
#             if page > 1:
#                 input = self.wait.until(
#                     EC.presence_of_element_located((By.CSS_SELECTOR, '#mainsrp-pager div.form > input')))
#                 submit = self.wait.until(
#                     EC.element_to_be_clickable((By.CSS_SELECTOR, '#mainsrp-pager div.form > span.btn.J_Submit')))
#                 input.clear()
#                 input.send_keys(page)
#                 submit.click()
#             self.wait.until(
#                 EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#mainsrp-pager li.item.active > span'), str(page)))
#             self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.m-itemlist .items .item')))
#             return HtmlResponse(url=request.url, body=self.browser.page_source, request=request, encoding='utf-8',
#                                 status=200)
#         except TimeoutException:
#             return HtmlResponse(url=request.url, status=500, request=request)
