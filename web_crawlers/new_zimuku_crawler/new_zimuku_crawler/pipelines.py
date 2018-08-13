# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import os

class NewZimukuCrawlerPipeline(object):
	def process_item(self, item, spider):
		# Directory setup
		full_path = os.path.dirname(os.path.abspath(__file__))
		output_dir = os.path.join(full_path, 'results')

		if not os.path.isdir(output_dir):
			os.makedirs(output_dir)

		# Clean file name
		file_name = item['file_name']
		file_name = file_name.replace('/','_').replace(':','_')
		file_path = os.path.join(output_dir, file_name)

		# Write downloaded file to disk
		try:
			with open(file_path, 'wb+') as f:
				f.write(item['body'])
		except OSError as e:
			print("[ERROR]\tFile could not be opened or created. Skipping")

		return item
