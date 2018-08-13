import sys
import re
import os
import chardet
import codecs

from pathlib import Path

illegal = u"([\u0000-\u2010]+)"
illegal_patterns = [re.compile(u"([\u2000-\u2010]+)"), re.compile(u"([\u0090-\u0099]+)")]

filters = [
	"字幕",
	"时间轴:",
	"校对:",
	"翻译:",
	"后期:",
	"监制:",
	"禁止用作任何商业盈利行为",
	"http",
]

htmlagregex = re.compile(r'<[^>]+>', re.S)
brace_regex = re.compile(r'\{.*\}', re.S)
slash_regex = re.compile(r'\\\w', re.S)
repeat_regex = re.compile(r'[-=]{10}', re.S)

def purify(data_dir):
	pure_phrases = 0

	full_data_dir = Path(data_dir).resolve()
	input_file = os.path.join(full_data_dir, 'lang_filtered_full.txt')
	output_file = os.path.join(full_data_dir, 'purified_full.txt')

	try:
		with open(input_file, 'rb') as fr:
			print("[LOG]\tProcessing: " + input_file)
			data = fr.read()
	except OSError as e:
		print("[ERROR]\tInput file (lang_filtered_full.txt) could not be opened/found in Data directory. Skipping\n", file=sys.stderr)

	try:
		for phrase in codecs.decode(data, 'utf-8').split('\n'):
				phrase = phrase.strip()

				# Filter non-Chineses phrases
				need_continue = False
				for illegal_pattern in illegal_patterns:
					match_pattern = re.findall(illegal_pattern, phrase)
					if len(match_pattern) > 0:
						print("[LOG]\tPhrase: " + phrase + " <===> Phrase is not written in Chineses. Skipping\n", file=sys.stderr)
						need_continue = True
						break
				if need_continue:
					continue

				# Filter unwanted words
				need_continue = False
				for filt in filters:
					try:
						phrase.index(filt)
						print("[LOG]\tPhrase: " + phrase + " <===> Filter keyword: " + filt, file=sys.stderr)
						need_continue = True
						break
					except:
						pass
				if need_continue:
					continue

				# Filter episodic nomencalture
				if re.match('.*第.*季.*', phrase):
					print("[LOG]\tPhrase: " + phrase + " <===> Filter keyword: .*第.*季.*", file=sys.stderr)
					continue
				if re.match('.*第.*集.*', phrase):
					print("[LOG]\tPhrase: " + phrase + " <===> Filter keyword: .*第.*集.*", file=sys.stderr)
					continue
				if re.match('.*第.*帧.*', phrase):
					print("[LOG]\tPhrase: " + phrase + " <===> Filter keyword: .*第.*帧.*", file=sys.stderr)
					continue

				phrase = htmlagregex.sub('', phrase)
				phrase = brace_regex.sub('', phrase)
				phrase = slash_regex.sub('', phrase)

				new_phrase = repeat_regex.sub('', phrase)

				if not len(new_phrase) == len(phrase):
					continue

				phrase = phrase.replace('-', '').strip() 

				if len(phrase) > 0:
					try:
						with open(output_file, 'ab+') as fw:
							phrase = phrase + '\n'
							fw.write(codecs.encode(phrase, 'utf-8'))
							phrase = phrase.replace('\n', '')
							print("[LOG]\tPhrase: " + phrase + " <===> Written to file", file=sys.stderr)
							pure_phrases += 1
					except OSError as e:
						print("[ERROR]\tOutput file (purified_full.txt) could not be opened for writing. Skipping\n", file=sys.stderr)

	except Exception as e:
	print("[ERROR]\tInput file (lang_filtered_full.txt) must be in UTF-8 format. Skipping\n", file=sys.stderr)

	print("-------------------------")	
	print("[INFO]\tCorpus successfully purified")
	print("[INFO]\tPhrases extracted: " + str(pure_phrases) + "\n")
	

if __name__ == '__main__':
	# User parameters
	data_dir = ''

	# If only one argument is provided, assume Data directory and go with default length
	if len(sys.argv) == 2:
		data_dir = sys.argv[1]
	# Otherwise default to my Data directory
	else:
		data_dir = '.\Data'

	print("[INFO]\tBeginning purification...")
	purify(data_dir)