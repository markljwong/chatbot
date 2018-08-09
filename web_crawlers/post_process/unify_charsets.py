import os
import sys
import chardet
import codecs
import purge

acceptable_charsets = (
	'utf-8',
	'utf-8-sig',
	'utf-16-le'
)

def unify_charsets(path):
	for root, dirs, files in os.walk(path):
		for file in files:
			filepath = os.path.join(root, file)

			print("[INFO]\tProcessing: " + filepath)

			# Try to open file at filepath
			try:
				with codecs.open(filepath, 'rb') as f:
					data = f.read()
			except OSError:
				print("[ERROR]\tFile could not be opened or doesn't exist. Aborting.\n")
				exit(1)

			# Get current encoding of the file
			detect = chardet.detect(data)
			encoding = detect["encoding"]
			confidence = detect["confidence"]

			try:
				print("[INFO]\tEncoding: " + encoding + ", Confidence: " + str(confidence))
			except TypeError:
				print("[INFO]\tFile is empty.")

			# If it isn't UTF-8 or ASCII then decode and reencode it as UTF-8
			if encoding not in acceptable_charsets:
				# Try to write memory to disk
				try:
					with open(filepath, 'wb') as f:			
						data = codecs.decode(data, encoding)
						f.write(codecs.encode(data, 'utf-8'))
				except:
					print("[ERROR]\tFile could not be encoded. Skipping.")

	print("-------------------------")	
	print("\tAll files converted to UTF-8.")

def no_bom(path):
	for root, dirs, files in os.walk(path):
		for file in files:
			filepath = os.path.join(root, file)

			print("[INFO] Processing " + filepath)

			# Try to open file at filepath
			try:
				with codecs.open(filepath, 'rb') as f:
					data = f.read()
			except IOError:
				print("[ERROR]\tFile could not be opened or doesn't exist. Aborting.\n")
				exit(1)

			# Get current encoding of the file
			detect = chardet.detect(data)
			encoding = detect["encoding"]
			confidence = detect["confidence"]
			
			try:
				print("[INFO]\tEncoding: " + encoding + ", Confidence: " + str(confidence))
			except TypeError:
				print("[INFO]\tFile is empty.")

			# If data is encoded in UTF-8 then attempt to remove BOM, otherwise skip
			if encoding == 'utf-8' or encoding == 'utf-8-sig':
				try:
					with open(filepath, 'wb') as f:			
						data = codecs.decode(data, 'utf-8-sig')
						f.write(codecs.encode(data, 'utf-8'))
				except:
					print("[ERROR]\tFile could not be encoded. Skipping.")
			else:
				print("[ERROR]\tFile is not utf-8. Skipping ")

	print("-------------------------")	
	print("[INFO]\tAll files converted to UTF-8 with no BOM.\n")

if __name__ == '__main__':
	inputDir = ''

	# If user gives input, use that folder
	if len(sys.argv) == 2:
		inputDir = sys.argv[1]
	# Otherwise default to my directory format
	else:
		inputDir = './Data/sorted/'

	# Unify charsets
	unify_charsets(inputDir)

	# Clean empty files or directories left over
	print("[INFO]\tWould you like to purge empty files and directories in the subtitle folder?")
	print("[INFO]\t[Y]es, [N]o")

	purge_response = input("[INPUT]\tCommand: ")
	
	# See purge.py for details
	if purge_response == 'Y' or purge_response == 'y' or purge_response =='Yes' or purge_response == 'yes':
		print("[INFO]\tPurging subtitle folder...")
		for suffix in purge.purgatory:
			purge.purge_files(inputDir, suffix)

		dirPurged = purge.purge_empty_dirs(inputDir)

		print("-------------------------")
		print("[INFO]\tSubtitle folder purged.\n")

	else:
		print("-------------------------")
		print("[INFO]\tUser cancelled.\n")

	
	# Conver UTF-8 with BOM to no BOM
	print("[INFO]\tWould you like to convert all to UTF-8 with no BOM?")
	print("[INFO]\tWarning: Takes quite some time)")
	print("[INFO]\t[Y]es [N]o")
 
	bom_response = input("[INPUT]\tCommand: ")

	if bom_response == 'Y' or bom_response == 'y' or bom_response =='Yes' or bom_response == 'yes':
		print("[INFO]\tConverting to UTF-8 without BOM...")

		# If user gives input, use that folder
		if len(sys.argv) == 2:
			no_bom(sys.argv[1])
		# Otherwise default to my directory format
		else:
			no_bom('./Data/sorted')

	else:
		print("-------------------------")
		print("[INFO]\tUser cancelled.\n")

	print("-------------------------")
	print("[INFO]\tProcess finished.\n")