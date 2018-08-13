import os
import sys
import chardet
import codecs
import purge

acceptable_charsets = (
	'utf-8',
	'utf-8-sig',
)

def unify_charsets(data_dir):
	full_data_dir =Path(data_dir).resolve()
	input_dir = os.path.join(full_data_dir, 'sorted')

	for root, dirs, files in os.walk(input_dir):
		for file in files:
			filepath = os.path.join(root, file)

			print("[LOG]\tProcessing: " + filepath)

			try:
				with codecs.open(filepath, 'rb') as f:
					data = f.read()
			except OSError as e:
				print("[ERROR]\tFile: " + file + " <===> File could not be opened or doesn't exist. Skipping.\n")
				continue

			detect = chardet.detect(data)
			encoding = detect["encoding"]
			confidence = detect["confidence"]

			# File might be empty which returns encoding as NoneType which can't be concat to a string
			try:
				print("[LOG]\tFile: " + file + " <===> Encoding: " + encoding + ", Confidence: " + str(confidence))
			except TypeError as e:
				print("[ERROR]\tFile: " + file + " <===> File is empty. Cannot concat NoneType to String")

			# If it isn't an acceptable charset hen decode and reencode it as UTF-8
			if encoding not in acceptable_charsets:
				try:
					with open(filepath, 'wb') as f:			
						data = codecs.decode(data, encoding)
						f.write(codecs.encode(data, 'utf-8'))
						print("[LOG]\tFile: " + file + " <===> File successfully encoded as utf-8.\n")
				except Exception as e:
					print("[ERROR]\tFile: " + file + " <===> File could not be encoded. Skipping.\n")
					continue
			else:
				print("[LOG]\tFile: " + file + " <===> File is already acceptable. Skipping.\n")
				continue

	print("-------------------------")	
	print("[INFO]\tAll files converted to UTF-8.\n")

def no_bom(data_dir):
	full_data_dir = Path(data_dir).resolve()
	input_dir = os.path.join(full_data_dir, 'sorted')

	for root, dirs, files in os.walk(input_dir):
		for file in files:
			filepath = os.path.join(root, file)

			print("[LOG]\tProcessing " + filepath)

			try:
				with codecs.open(filepath, 'rb') as f:
					data = f.read()
			except OSError as e:
				print("[ERROR]\tFile: " + file + " <===> File could not be opened or doesn't exist. Aborting.\n")
				continue

			detect = chardet.detect(data)
			encoding = detect["encoding"]
			confidence = detect["confidence"]
			
			# File might be empty which returns encoding as NoneType which can't be concat to a string
			try:
				print("[LOG]\tFile: " + file + " <===> Encoding: " + encoding + ", Confidence: " + str(confidence))
			except TypeError as e:
				print("[LOG]\tFile: " + file + " <===> File is empty.")

			# If data is encoded in UTF-8 then attempt to remove BOM, otherwise skip
			if encoding == 'utf-8' or encoding == 'utf-8-sig':
				try:
					with open(filepath, 'wb') as f:			
						data = codecs.decode(data, 'utf-8-sig')
						f.write(codecs.encode(data, 'utf-8'))
						print("[LOG]\tFile: " + file + " <===> File successfully un-BOM-ified.\n")
				except Exception as e:
					print("[ERROR]\tFile: " + file + " <===> File could not be encoded. Skipping.\n")
					continue
			else:
				print("[LOG]\tFile: " + file + " <===> File is not utf-8. Skipping.\n")
				continue

	print("-------------------------")	
	print("[INFO]\tAll files converted to UTF-8 with no BOM.\n")

if __name__ == '__main__':
	data_dir = ''
	do_purge = False
	do_no_bom = False

	# If user gives input, use that as Data directory
	if len(sys.argv) == 2:
		data_dir = sys.argv[1]
	# Otherwise default to my directory format
	else:
		data_dir = '.\Data'

	print("[INFO]\tWould you like to purge empty files and directories after process completes?")
	print("[INFO]\t[Y]es, [N]o\n")

	purge_response = input("[INPUT]\tCommand: ")
	
	if purge_response == 'Y' or purge_response == 'y' or purge_response =='Yes' or purge_response == 'yes':
		print("[INFO]\tWill purge directories and files after process completes.\n")
		do_purge = True
	else:
		print("[INFO]\tWill NOT purge directories and files after process completes.\n")

	print("[INFO]\tWould you like to convert all to UTF-8 with no BOM?")
	print("[INFO]\tWarning: Takes quite some time)")
	print("[INFO]\t[Y]es [N]o\n")
 
	bom_response = input("[INPUT]\tCommand: ")

	if bom_response == 'Y' or bom_response == 'y' or bom_response =='Yes' or bom_response == 'yes':
		print("[INFO]\tWill de-BOM applicable UTF-8 files.\n")
		do_purge = True
	else:
		print("[INFO]\tWill NOT de-BOM applicable UTF-8 files.\n")

	print("[INFO]\tBeginning filtration...\n")
		
	unify_charsets(data_dir)

	if do_no_bom:
		print("[INFO]\tConverting to UTF-8 without BOM...")
		no_bom(data_dir)

	if do_purge:
		print("[INFO]\tPurging subtitle directory...")
		for suffix in purge.purgatory:
			purge.purge_files(data_dir, suffix)
		purge.purge_empty_dirs(data_dir)

	print("-------------------------")
	print("[INFO]\tProcess finished.\n")