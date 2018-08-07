# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

class ZimukuCrawlerPipeline(object):
	def process_item(self, item, spider):
		# Clean file name
		fileName = item['fileName']
		fileName = fileName.replace('/','_').replace(':','_')

		# Write downloaded file to diks
		fp = open('results/' + fileName, 'wb')
		fp.write(item['body'])
		fp.close()
		
		return item