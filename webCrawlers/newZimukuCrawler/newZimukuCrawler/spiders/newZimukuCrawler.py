import scrapy

from w3lib.html import remove_tags
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor
from newZimukuCrawler.items import NewZimukuCrawlerItem

class newZimukuCrawler(scrapy.Spider):
	name = "newZimukuCrawler"
	allowed_domains = [
		"zimuku.cn",
		"subku.net",
	]
	start_urls = [
		"https://www.zimuku.cn/search?q=&p=1",
	]

	rules = (
		Rule(LinkExtractor(allow=('\.htm'))),
	)

	def parse(self, response):
		# Find containers for download page link and file name
		containers = response.selector.xpath('//div[contains(@class, "item prel")]/div[contains(@class, "title")]/div/table/tbody/tr/td[contains(@class, "first")]')

		# Go through all containers 
		for container in containers:
			# Get file name for that specific file
			fileName = container.xpath('a/@title')[0].extract()

			# Assign file name to new item
			item = NewZimukuCrawlerItem()
			item['fileName'] = fileName

			# Get link to download page
			href = container.xpath('a/@href')[0].extract()

			# Go to download page
			url = response.urljoin(href)
			request = scrapy.Request(url, callback = self.parse_detail)
			request.meta['item'] = item
			yield request

	# Download page for a specific subtitle
	def parse_detail(self, response):
		# Get link to provider selection page
		url = response.selector.xpath('//li[contains(@class, "dlsub")]/div/a[contains(@id, "down1")]/@href').extract()[0]

		# Go to provider selection page
		request = scrapy.Request(url, callback = self.parse_download) 
		request.meta['item'] = response.meta['item']
		yield request

	# Webpage that opens to select provider
	def parse_download(self, response):
		# Get url to actual file download
		url = response.selector.xpath('//div[contains(@class, "down")]/ul/li/a/@href').extract()[4]

		# Download file
		request = scrapy.Request(url, callback = self.parse_file)
		request.meta['item'] = response.meta['item']
		yield request

	def parse_file(self, response):
		body = response.body
		item = response.meta['item']
		item['body'] = body
		return item
