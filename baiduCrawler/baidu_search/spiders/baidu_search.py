import scrapy

from html.parser import HTMLParser

class MLStripper(HTMLParser):
	def __init__(self):
		self.reset()
		self.strict = False
		self.convert_charrefs= True
		self.fed = []
	def handle_data(self, d):
		self.fed.append(d)
	def get_data(self):
		return ''.join(self.fed)

def strip_tags(html):
	s = MLStripper()
	s.feed(html)
	return s.get_data()

class BaiduSearchSpider(scrapy.Spider):
	name = "baidu_search"
	allowed_domains = ["baidu.com"]
	start_urls = [
		"https://www.baidu.com/s?wd=机器学习"
	]

	def parse(self, response):
		filename = "result.html"
		with open(filename, 'wb') as f:
			f.write(response.body)

		hrefs = response.selector.xpath('//div[contains(@class, "c-container")]/h3/a/@href').extract()
		containers = response.selector.xpath('//div[contains(@class, "c-container")]')

		for container in containers:
			href = container.xpath('h3/a/@href').extract()[0]
			title = strip_tags(container.xpath('h3/a').extract()[0])
			c_abstract = container.xpath('div/div/div[contains(@class, "c-abstract")]').extract()
			abstract = ""

			if len(c_abstract) > 0:
				abstract = strip_tags(c_abstract[0])

			request = scrapy.Request(href, callback=self.parse_url)
			request.meta['title'] = title
			request.meta['abstract'] = abstract

			yield request

	def parse_url(self, response):
		print("url: " + response.url)
		print("title: " + response.meta['title'])
		print("abstract: " + response.meta['abstract'])
		content = strip_tags(response.selector.xpath('//body').extract()[0])
		print("content_len: " + repr(len(content)))

