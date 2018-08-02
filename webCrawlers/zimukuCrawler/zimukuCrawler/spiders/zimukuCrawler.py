import scrapy

from w3lib.html import remove_tags
from zimukuCrawler.items import ZimukuCrawlerItem

class zimukuCrawler(scrapy.Spider):
	name = "zimukuCrawler"
	allowed_domains = ["zimuku.cn"]
	start_urls = [
		"http://www.zimuku.cn/search?q=&t=onlyst&ad=1&p=20",
		"http://www.zimuku.cn/search?q=&t=onlyst&ad=1&p=21",
		"http://www.zimuku.cn/search?q=&t=onlyst&ad=1&p=22",
	]

	def parse(self, response):
		hrefs = response.selector.xpath('//div[contains(@class, "persub")]/h1/a/@href').extract()
		for href in hrefs:
			url = response.urljoin(href)
			print("url: " + url)
			request = scrapy.Request(url, callback = self.parse_detail)
			yield request

	def parse_detail(self, response):
		self.logger.info('parse_detail request 1\n')
		url = response.selector.xpath('//li[contains(@class, "dlsub")]/div/a/@href').extract()[0]
		print("processing: " + url)
		yield scrapy.Request(url, callback = self.parse_file) 

	def parse_file(self, response):
		body = response.body
		item = ZimukuCrawlerItem()
		item['url'] = response.url
		item['body'] = body
		return item