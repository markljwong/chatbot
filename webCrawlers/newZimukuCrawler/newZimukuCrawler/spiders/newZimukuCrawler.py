import scrapy

from w3lib.html import remove_tags
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor
from newZimukuCrawler.items import NewZimukuCrawlerItem

class newZimukuCrawler(scrapy.Spider):
	name = "newZimukuCrawler"
	allowed_domains = ["zimuku.cn"]
	start_urls = [
		"https://www.zimuku.cn/search?q=&p=1",
	]

	rules = (
		Rule(LinkExtractor(allow=('\.htm'))),
	)

	def parse(self, response):
		# Find all containers for unique downloads
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
		print("processing: " + url)

		# Download file and then go parse the file
		request = scrapy.Request(url, callback = self.parse_file) 
		request.meta['item'] = response.meta['item']

		yield request

	def parse_file(self, response):
		body = response.body
		item = response.meta['item']
		item['url'] = response.url
		item['body'] = body
		return item
