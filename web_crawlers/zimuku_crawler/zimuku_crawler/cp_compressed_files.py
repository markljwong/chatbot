import os
import shutil

def movefile(inputDir, filetype='zip', counter=0):
	# Set destination folder name to be file type
	destination = "./" + filetype

	# Check if folder already exists
	dirExists = 0
	for dir in os.listdir():
		if dir == filetype:
			dirExists = 1

	# Create folder if it doens't exist yet
	if dirExists == 0:
		os.makedirs(destination)

	# Iterate through input directory and move applicable files to the new folder
	for pack in os.walk(inputDir):
		for file in pack[2]:
			if file.endswith(filetype):
				fullpath = pack[0] + "/" + file
				print(fullpath)
				shutil.copy(fullpath, destination)
				counter += 1
	if counter > 0:
		print("-------------------------")
		print("\t==> Found in: " + inputDir + " : " + str(counter) + " files\n")

movefile('results', 'zip')
movefile("results", 'rar')