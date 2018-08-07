import scrapy

from w3lib.html import remove_tags
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor
from zimuku_crawler.items import ZimukuCrawlerItem

class ZimukuCrawler(scrapy.Spider):
	name = "zimuku_crawler"
	allowed_domains = ["zimuku.cn"]
	start_urls = [
		"http://www.zimuku.cn/search?q=&t=onlyst&ad=1&p=1",
		"http://www.zimuku.cn/search?q=&t=onlyst&ad=1&p=2",
		"http://www.zimuku.cn/search?q=&t=onlyst&ad=1&p=3",
		"http://www.zimuku.cn/search?q=&t=onlyst&ad=1&p=4",
		"http://www.zimuku.cn/search?q=&t=onlyst&ad=1&p=5",
		"http://www.zimuku.cn/search?q=&t=onlyst&ad=1&p=6",
		"http://www.zimuku.cn/search?q=&t=onlyst&ad=1&p=7",
		"http://www.zimuku.cn/search?q=&t=onlyst&ad=1&p=8",
		"http://www.zimuku.cn/search?q=&t=onlyst&ad=1&p=9",
		"http://www.zimuku.cn/search?q=&t=onlyst&ad=1&p=10",
		"http://www.zimuku.cn/search?q=&t=onlyst&ad=1&p=11",
		"http://www.zimuku.cn/search?q=&t=onlyst&ad=1&p=12",
		"http://www.zimuku.cn/search?q=&t=onlyst&ad=1&p=13",
		"http://www.zimuku.cn/search?q=&t=onlyst&ad=1&p=14",
		"http://www.zimuku.cn/search?q=&t=onlyst&ad=1&p=15",
		"http://www.zimuku.cn/search?q=&t=onlyst&ad=1&p=16",
		"http://www.zimuku.cn/search?q=&t=onlyst&ad=1&p=17",
		"http://www.zimuku.cn/search?q=&t=onlyst&ad=1&p=18",
		"http://www.zimuku.cn/search?q=&t=onlyst&ad=1&p=19",
		"http://www.zimuku.cn/search?q=&t=onlyst&ad=1&p=20",
	]

	rules = (
		Rule(LinkExtractor(allow=('\.htm'))),
	)

	def parse(self, response):
		# Find containers for download page link and file name
		containers = response.selector.xpath('//div[contains(@class, "persub")]')

		# Go through all containers 
		for container in containers:
			# Get file name for that specific file
			fileName = container.xpath('p/span')[0].extract()
			fileName = fileName[16:-7]

			# Assign file name to new item
			item = ZimukuCrawlerItem()
			item['fileName'] = fileName

			# Get link to download page for that specific file
			href = container.xpath('h1/a/@href')[0].extract()

			# Go to download page
			url = response.urljoin(href)
			request = scrapy.Request(url, callback = self.parse_detail)
			request.meta['item'] = item
			yield request

	def parse_detail(self, response):
		# Get url to actual file download
		url = response.selector.xpath('//li[contains(@class, "dlsub")]/div/a/@href').extract()[0]

		# Download file and then go parse the file
		request = scrapy.Request(url, callback = self.parse_file) 
		request.meta['item'] = response.meta['item']

		yield request

	def parse_file(self, response):
		body = response.body
		item = response.meta['item']
		item['body'] = body
		return item
