import re
import os
import sys
import chardet
import codecs

from pathlib import Path

cn=u"([\u4e00-\u9fa5]+)"
pattern_cn = re.compile(cn)
jp1=u"([\u3040-\u309F]+)"
pattern_jp1 = re.compile(jp1)
jp2=u"([\u30A0-\u30FF]+)"
pattern_jp2 = re.compile(jp2)

def filter_language_srt(data_dir, single_file = False, length = 16):
	# Counter for phrases of acceptable language
	lang_phrases = 0

	full_data_dir = Path(data_dir).resolve()
	output_dir = full_data_dir
	input_dir = os.path.join(full_data_dir, 'sorted', 'srt')

	if not os.path.isdir(output_dir):
		os.makedirs(output_dir)
 
	for root, dirs, files in os.walk(input_dir):
		file_count = len(files)
		if file_count > 0:
			for index, file in enumerate(files):
				filepath = os.path.join(root, file)

				# Generate new file to store filtered Chinese text
				if single_file:
					new_filename = "lang_filtered_full.txt"
				else:
					new_filename = file[:-4] + ".txt"
				new_filepath = os.path.join(output_dir, new_filename)

				print("[LOG]\tProcessing: " + filepath, file=sys.stderr)

				try:
					with open(filepath, 'rb') as f:
						data = f.read()
				except OSError as e:
					print("[ERROR]\tFile: " + file + " <===> File could not be opened. Skipping\n", file=sys.stderr)
					continue
	
				encoding = chardet.detect(data)["encoding"]
				print("[LOG]\tFile: " + file + " <===> Encoding: " + encoding, file=sys.stderr)

				try:
					for phrase in codecs.decode(data, encoding).split('\n'):
						print("[LOG]\tFile: " + file + " <===> Phrase: " + phrase, file=sys.stderr)
						if len(phrase) > 0:
							# Test for Chinese but also for Japanese, since they use the same format and we don't want Japanese
							match_cn =  re.findall(pattern_cn, phrase)
							match_jp1 =  re.findall(pattern_jp1, phrase)
							match_jp2 =  re.findall(pattern_jp2, phrase)

							# Phrase must have Chinese, no Japanese and acceptable length to be written to file
							if len(match_cn) > 0 and len(match_jp1) == 0 and len(match_jp2) == 0 and len(phrase) < length:
								phrase = phrase.strip()
								print("[LOG]\tFile: " + file + " <===> Phrase: " + phrase + " <===> Accepted", file=sys.stderr)
								try:
									with open(new_filepath, 'ab+') as f:
										f.write(codecs.encode(phrase, 'utf-8'))
										f.write(codecs.encode('\n', 'utf-8'))
										print("[LOG]\tFile: " + file + " <===> Phrase: " + phrase + " <===> Written to file", file=sys.stderr)
										lang_phrases += 1
								except OSError as e:
									print("[ERROR]\tFile: " + file + " <===> Output file could not be created or opened. Skipping\n", file=sys.stderr)
									continue
							else:
								phrase = phrase.replace('\n', '')
								print("[LOG]\tFile: " + file + " <===> Phrase: " + phrase + " <===> Denied", file=sys.stderr)
				except Exception as e:
					print("[ERROR]\tFile: " + file + " <===> File could not be decoded. Skipping\n", file=sys.stderr)
					continue

	print("-------------------------")	
	print("[INFO]\tLanguages successfully extracted from .srt files")
	print("[INFO]\tPhrases extracted: " + str(lang_phrases) + "\n")

	return lang_phrases

def filter_language_ssa(data_dir, single_file = False, length = 16):
	# Counter for phrases of acceptable language
	lang_phrases = 0

	full_data_dir = Path(data_dir).resolve()
	output_dir = full_data_dir
	input_dir = os.path.join(full_data_dir, 'sorted', 'ssa')

	if not os.path.isdir(output_dir):
		os.makedirs(output_dir)
 
	for root, dirs, files in os.walk(input_dir):
		file_count = len(files)
		if file_count > 0:
			for index, file in enumerate(files):
				filepath = os.path.join(root, file)

				# Generate new file to store filtered Chinese text
				if single_file:
					new_filename = "lang_filtered_full.txt"
				else:
					new_filename = file[:-4] + ".txt"
				new_filepath = os.path.join(output_dir, new_filename)

				print("[LOG]\tProcessing: " + filepath, file=sys.stderr)

				try:
					with open(filepath, 'rb') as f:
						data = f.read()
				except OSError as e:
					print("[ERROR]\tFile: " + file + " <===> File could not be opened. Skipping\n", file=sys.stderr)
					continue

				encoding = chardet.detect(data)["encoding"]
				print("[LOG]\tFile: " + file + " Encoding: " + encoding, file=sys.stderr)

				try:
					for line in re.split('\n', codecs.decode(data, encoding)):
						if not line.find('Dialogue') == -1:
							# Get valid phrases
							fields = re.split(',', line)
							field = fields[len(fields)-1]
							phrases = re.split('}', field)

							for phrase in phrases:
								print("[LOG]\tFile: " + file + " <===> Phrase: " + phrase, file=sys.stderr)		

								# Test for Chinese but also for Japanese, since they use the same format and we don't want Japanese
								match_cn =  re.findall(pattern_cn, phrase)
								match_jp1 =  re.findall(pattern_jp1, phrase)
								match_jp2 =  re.findall(pattern_jp2, phrase)

								# Phrase must have Chinese, no Japanese and acceptable length to be written to file
								if len(match_cn) > 0 and len(match_jp1) == 0 and len(match_jp2) == 0 and len(phrase) < length:
									phrase = phrase.strip()
									phrase = phrase.replace('\n', '')
									print("[LOG]\tFile: " + file + " <===> Phrase: " + phrase + " <===> Accepted")
									try:
										with open(new_filepath, 'ab+') as f:
											f.write(codecs.encode(phrase, 'utf-8'))
											f.write(codecs.encode('\n', 'utf-8'))
											print("[LOG]\tFile: " + file + " <===> Phrase: " + phrase + " <===> Written to file", file=sys.stderr)
											lang_phrases += 1
									except OSError as e:
										print("[ERROR]\tFile: " + file + " <===> Output file could not be created or opened. Skipping\n", file=sys.stderr)
										continue
								else:
									phrase = phrase.replace('\n', '')
									print("[LOG]\tFile: " + file + " <===> Phrase: " + phrase + " <===> Denied", file=sys.stderr)
				except Exception as e:
					print("[ERROR]\tFile: " + file + " <===> File could not be decoded. Skipping\n", file=sys.stderr)
					continue

	print("-------------------------")	
	print("[INFO]\tLanguages successfully extracted from .ssa files")
	print("[INFO]\tLines extracted: " + str(lang_phrases) + "\n")

	return lang_phrases


def filter_language_ass(data_dir, single_file = False, length = 16):
	# Counter for phrases of acceptable language
	lang_phrases = 0

	full_data_dir = Path(data_dir).resolve()
	output_dir = full_data_dir
	input_dir = os.path.join(full_data_dir, 'sorted', 'ass')

	# Check if output_dir already exists, if not, make it
	if not os.path.isdir(output_dir):
		os.makedirs(output_dir)
 
	for root, dirs, files in os.walk(input_dir):
		file_count = len(files)
		if file_count > 0:
			for index, file in enumerate(files):
				filepath = os.path.join(root, file)

				# Generate new file to store filtered Chinese text
				if single_file:
					new_filename = "lang_filtered_full.txt"
				else:
					new_filename = file[:-4] + ".txt"
				new_filepath = os.path.join(output_dir, new_filename)

				print("[LOG]\tProcessing: " + filepath, file=sys.stderr)

				try:
					with open(filepath, 'rb') as f:
						data = f.read()
				except OSError as e:
					print("[ERROR]\tFile: " + file + " <===> File could not be opened. Skipping\n", file=sys.stderr)
					continue
		
				encoding = chardet.detect(data)["encoding"]
				print("[LOG]\tFile: " + file + " <===> Encoding: " + encoding, file=sys.stderr)

				try:
					for line in re.split('\n', codecs.decode(data, encoding)):
						if not line.find('Dialogue') == -1:
							# Get valid phrases
							fields = re.split(',', line)
							field = fields[len(fields)-1]
							phrases = re.split('}', field)

							for phrase in phrases:
								print("[LOG]\tFile: " + file + " <===> Phrase: " + phrase, file=sys.stderr)		

								# Test for Chinese but also for Japanese, since they use the same format and we don't want Japanese
								match_cn =  re.findall(pattern_cn, phrase)
								match_jp1 =  re.findall(pattern_jp1, phrase)
								match_jp2 =  re.findall(pattern_jp2, phrase)

								# Phrase must have Chinese, no Japanese and acceptable length to be written to file
								if len(match_cn) > 0 and len(match_jp1) == 0 and len(match_jp2) == 0 and len(phrase) < length:
									phrase = phrase.strip()
									phrase = phrase.replace('\n', '')
									print("[LOG]\tFile: " + file + " <===> Phrase: " + phrase + " <===> Accepted", file=sys.stderr)
									try:
										with open(new_filepath, 'ab+') as f:
											f.write(codecs.encode(phrase, 'utf-8'))
											f.write(codecs.encode('\n', 'utf-8'))
											print("[LOG]\tFile: " + file + " <===> Phrase: " + phrase + " <===> Written to file", file=sys.stderr)
											lang_phrases += 1
									except OSError as e:
										print("[ERROR]\tFile: " + file + " <===> Output file could not be created or opened. Skipping\n", file=sys.stderr)
										continue
								else:
									phrase = phrase.replace('\n', '')
									print("[LOG]\tFile: " + file + " <===> Phrase: " + phrase + " <===> Denied", file=sys.stderr)
				except Exception as e:
					print("[ERROR]\tFile: " + file + " <===> File could not be decoded. Skipping\n", file=sys.stderr)
					continue

	print("-------------------------")	
	print("[INFO]\tLanguages successfully extracted from .ass files")
	print("[INFO]\tLines extracted: " + str(lang_phrases) + "\n")

	return lang_phrases

if __name__ == '__main__':
	# User parameters
	data_dir = ''
	output_dir = ''
	single_file = False
	length = 16

	# Booleans to know whether to filter this subtitle type
	filter_srt = False
	filter_ssa = False
	filter_ass = False

	# Counters
	total_lang_phrases = 0

	# If only one argument is provided, assume Data directory and go with default length
	if len(sys.argv) == 2:
		data_dir = sys.argv[1]
	# If user gives two args, assume first is Data directory and second is length
	elif len(sys.argv) == 3:
		data_dir = sys.argv[1]
		length = int(sys.argv[2])
	# Otherwise default to my Data directory
	else:
		data_dir = '.\Data'

	print("[INFO]\tFilter .srt files for language?")
	print("[INFO]\t[Y]es, [N]o\n")

	srt_response = input("[INPUT]\tCommand: ")

	if srt_response == 'Y' or srt_response == 'y' or srt_response =='Yes' or srt_response == 'yes':
		print("[INFO]\tWill filter .srt files.\n")
		filter_srt = True
	else:
		print("[INFO]\tWill NOT filter .srt files.\n")

	print("[INFO]\tFilter .ssa files for language?")
	print("[INFO]\t[Y]es, [N]o\n")

	ssa_response = input("[INPUT]\tCommand: ")

	if ssa_response == 'Y' or ssa_response == 'y' or ssa_response =='Yes' or ssa_response == 'yes':
		print("[INFO]\tWill filter .ssa files.\n")
		filter_ssa = True
	else:
		print("[INFO]\tWill NOT filter .ssa files.\n")

	print("[INFO]\tFilter .ass files for language?")
	print("[INFO]\t[Y]es, [N]o\n")

	ass_response = input("[INPUT]\tCommand: ")

	if ass_response == 'Y' or ass_response == 'y' or ass_response =='Yes' or ass_response == 'yes':
		print("[INFO]\tWill filter .ass files.\n")
		filter_ass = True
	else:
		print("[INFO]\tWill NOT filter .ass files.\n")

	print("[INFO]\tCollect all phrases in one file (If not, then each subtitle file will have its own output file?")
	print("[INFO]\tNote: To perform further processing, file MUST be in one file format.")
	print("[INFO]\t[Y]es, [N]o\n")

	sin_file_response = input("[INPUT]\tCommand: ")

	if sin_file_response == 'Y' or sin_file_response == 'y' or sin_file_response =='Yes' or sin_file_response == 'yes':
		print("[INFO]\tWill collect all phrases in one file.\n")
		single_file = True
	else:
		print("[INFO]\tWill NOT collect all phrases in one file.\n")

	print("[INFO]\tBeginning filtration...\n")

	# Begin filterring
	if filter_srt == True:
		print("[INFO]\tFilterring .srt...\n")
		total_lang_phrases += filter_language_srt(data_dir, single_file, length)

	if filter_ssa == True:
		print("[INFO]\tFilterring .ssa...\n")
		total_lang_phrases += filter_language_ssa(data_dir, single_file, length)

	if filter_ass == True:
		print("[INFO]\tFilterring .ass...\n")
		total_lang_phrases += filter_language_ass(data_dir, single_file, length)

	print("-------------------------")	
	print("[INFO]\tTotal languages successfully extracted from selected files")
	print("[INFO]\tPhrases extracted: " + str(total_lang_phrases) + "\n")