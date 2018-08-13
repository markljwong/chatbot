import os
import sys

# NOTE: Feel free to add more as needed. The program should still handle them
# Unwanted file formats
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
def purge_files(data_dir, suffix):
	# Counter for unwanted and empty files
	u_counter = 0
	e_counter = 0

	print("[LOG]\tProcessing: " + data_dir, file=sys.stderr)

	for root, dirs, files in os.walk(data_dir):
		for directory in dirs:
			purge_files(os.path.join(root, directory), suffix)
		for file in files:
			filepath = os.path.join(root, file)
			if filepath.endswith(suffix):
				print("[LOG]\tDirectory: " + root + " <===> Removed unwanted file " + file, file=sys.stderr)
				os.remove(filepath)
				u_counter += 1
			if os.stat(filepath).st_size == 0:
				print("[LOG]\tDirectory: " + root + " <===> Removed empty file " + file, file=sys.stderr)
				os.remove(filepath)
				e_counter += 1

	print("-------------------------")	
	print("[INFO]\tFile purge successfully completed for type: " + suffix)
	print("[INFO]\tUnwanted files: " + str(u_counter) + ", Empty files: " + str(e_counter) + "\n")


# Return the abandoned homes to dust after the cleansing fires has burnt all who deserve it
def purge_empty_dirs(data_dir):
	# Counter for removed directories
	dir_counter = 0

	print("[LOG]\tProcessing: " + data_dir, file=sys.stderr)
	for root, dirs, files in os.walk(data_dir):
		for directory in dirs:
			purge_empty_dirs(os.path.join(root, directory))
		if len(files) == 0 and len(dirs) == 0:
			print("[LOG]\tRemoved directory at " + root, file=sys.stderr)
			os.rmdir(root)
			dir_counter += 1

	print("-------------------------")	
	print("[INFO]\tDirectory purge successfully completed.")
	print("[INFO]\tEmpty directories: " + str(dir_counter) + "\n")

if __name__ == '__main__':
	data_dir = ''

	# If user gives input, use that as Data directory
	if len(sys.argv) == 2:
		data_dir = sys.argv[1]
	# Otherwise default to my Data directory
	else:
		data_dir = './Data'

	for suffix in purgatory:
		purge_files(data_dir, suffix)

	purge_empty_dirs(data_dir)