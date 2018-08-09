import os
import sys

# Useless file formats
purgatory = (
	'.mp4',
	'.txt',
	'.JPG',
	'.htm',
	'.doc',
	'.docx',
	'.nfo',
	'.sub',
	'.idx',
	'.ttf',
	'.TTF',
	'.SRT',
	'.SMI',
	'.TXT',
)

# Condemn those who sinned to god's inferno and burn away the soulless
# with recursion so that the fire may reach even those who hide in the dark
def purge_files(path, suffix):
	for root, dirs, files in os.walk(path):
		for directory in dirs:
			purge_files(root + directory, suffix)
		for file in files:
			filepath = root + '/' + file
			if filepath.endswith(suffix):
				print("[INFO]\tRemoved unwanted file at " + filepath)
				os.remove(filepath)
			if os.stat(filepath).st_size == 0:
				print("[INFO]\tRemoved empty file at " + filepath)
				os.remove(filepath)

# Return the abandoned homes to dust after the cleansing fires has burnt all who deserve it
def purge_empty_dirs(path):
	dirPurged = False
	for root, dirs, files in os.walk(path):
		for directory in dirs:
			purge_empty_dirs(root + directory)
		if len(files) == 0 and len(dirs) == 0:
			print("[INFO]\tRemoved directory at " + root)
			os.rmdir(root)
			dirPurged = True

	return dirPurged

if __name__ == '__main__':
	inputDir = ''

	# If user gives input, use that folder
	if len(sys.argv) == 2:
		inputDir = sys.argv[1]
	# Otherwise default to my directory format
	else:
		inputDir = './Data/extracted/'
		inputDir = './Data/sorted/'

	# Purge needless files
	for suffix in purgatory:
		purge_files(inputDir, suffix)

	# When no directories are purged, quit loop since it should be finished
	dirPurged = purge_empty_dirs(inputDir)