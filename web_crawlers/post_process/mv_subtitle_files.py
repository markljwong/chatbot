import os
import shutil
import sys

def mv_subtitle_files(inputDir, outputDir, filetype):
	counter = 0

	# Set destination folder name
	destination = outputDir + filetype

	# Check if outputDir already exists, if not, make it
	if not os.path.isdir(outputDir):
		os.makedirs(outputDir)

	# Check if subtitle directory within outpurDir already exists, if not, make it
	if not os.path.isdir(destination):
		os.makedirs(destination)

	# Iterate through input directory and move applicable files to the new folder
	for root, dirs, files in os.walk(inputDir):
		for file in files:
			if file.endswith(filetype):
				print(file)
				shutil.movefile(os.path.join(root, file), os.path.join(destination, file))
				counter += 1

	# Output how many of given filetype is found
	if counter > 0:
		print("-------------------------")
		print("[INFO}\tFound in: " + inputDir + " : " + str(counter) + " files\n")

if __name__ == '__main__':
	# If user gives input, use that folder
	if len(sys.argv) == 3:
		mv_subtitle_files(sys.argv[1], sys.argv[2], 'ass')
		mv_subtitle_files(sys.argv[1], sys.argv[2], 'lrc')
		mv_subtitle_files(sys.argv[1], sys.argv[2], 'smi')
		mv_subtitle_files(sys.argv[1], sys.argv[2], 'srt')
		mv_subtitle_files(sys.argv[1], sys.argv[2], 'ssa')
		mv_subtitle_files(sys.argv[1], sys.argv[2], 'str')
		mv_subtitle_files(sys.argv[1], sys.argv[2], 'sup')
		mv_subtitle_files(sys.argv[1], sys.argv[2], 'vtt')
	# If only one argument is provided, don't do anything:
	# Can't be sure if user's argument is their intended input or output directory
	elif len(sys.argv) == 2:
		print("[ERROR]\tUser must provide both input and output directory or neither for default raw location")
	# Otherwise default to my file directory format
	else:
		mv_subtitle_files('./Data/extracted', './Data/sorted/', 'ass')
		mv_subtitle_files('./Data/extracted', './Data/sorted/', 'smi')
		mv_subtitle_files('./Data/extracted', './Data/sorted/', 'srt')
		mv_subtitle_files('./Data/extracted', './Data/sorted/', 'ssa')
		mv_subtitle_files('./Data/extracted', './Data/sorted/', 'str')
		mv_subtitle_files('./Data/extracted', './Data/sorted/', 'sup')
		mv_subtitle_files('./Data/extracted', './Data/sorted/', 'vtt')