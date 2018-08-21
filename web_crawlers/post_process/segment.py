import sys
import re
import os
import codecs
import jieba

from pathlib import Path
from jieba import analyse

def segment(data_dir):
	full_data_dir = Path(data_dir).resolve()
	input_file = os.path.join(full_data_dir, 'purified_full.txt')
	output_file = os.path.join(full_data_dir, 'segmented_full.txt')

	try:
		with open(input_file, 'rb') as fr:
			print("[LOG]\tProcessing: " + input_file)
			data_in = fr.read()
	except OSError as e:
		print("[ERROR]\tInput file (purified_full.txt) could not be opened/found in data directory. Skipping\n", file=sys.stderr)

	# try:
	for phrase in codecs.decode(data_in, 'utf-8').split('\n'):
		if phrase:
			print("[LOG]\tProcesing Phrase: " + phrase, file=sys.stderr)
			phrase = phrase.strip()
			seg_list = jieba.cut(phrase)
			data_out = ""
			try:
				with open(output_file, 'ab+') as fw:
					for seg in seg_list:
						data_out = data_out + " " + seg
					fw.write(codecs.encode(data_out, 'utf-8'))
			except OSError as e:
					print("[ERROR]\tOutput file (purified_full.txt) could not be opened for writing. Skipping\n", file=sys.stderr)
		else:
			print("[LOG]\tFile: " + input_file + "\n\t\t\t\t\t\t\t\t <===> Processing complete\n", file=sys.stderr)
			break
	# except Exception as e:
	# 	print("[FATAL]\tInput file (lang_filtered_full.txt) must be in UTF-8 format. Quitting\n", file=sys.stderr)
	# 	exit(1)

if __name__ == '__main__':
	# User parameters
	data_dir = ''

	# If only one argument is provided, assume Data directory and go with default length
	if len(sys.argv) == 2:
		data_dir = sys.argv[1]
	# Otherwise default to my Data directory
	else:
		data_dir = '.\Data'

	segment(data_dir)