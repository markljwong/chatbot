import os
import shutil
import sys

def cp_subtitle_files(data_dir, filetype):
	counter = 0

	full_data_dir =Path(data_dir).resolve()
	input_dir = os.path.join(full_data_dir, 'extracted')
	output_dir = os.path.join(full_data_dir, "sorted")
	filetype_dir = os.path.join(output_dir, fileType)

	if not os.path.isdir(output_dir):
		os.makedirs(output_dir)
	if not os.path.isdir(filetype_dir):
		os.makedirs(filetype_dir)
	
	# Iterate through input directory and copy applicable files to the new directory
	for root, dirs, files in os.walk(input_dir):
		for file in files:
			if file.endswith(filetype):
				print(file)
				shutil.copyfile(os.path.join(root, file), os.path.join(filetype_dir, file))
				counter += 1

	if counter > 0:
		print("-------------------------")
		print("[INFO}\tFound in: " + input_dir + " : " + str(counter) + " files\n")

if __name__ == '__main__':
	# If user gives input, use that as Data directory
	if len(sys.argv) == 2:
		cp_subtitle_files(sys.argv[1], 'ass')
		cp_subtitle_files(sys.argv[1], 'lrc')
		cp_subtitle_files(sys.argv[1], 'smi')
		cp_subtitle_files(sys.argv[1], 'srt')
		cp_subtitle_files(sys.argv[1], 'ssa')
		cp_subtitle_files(sys.argv[1], 'str')
		cp_subtitle_files(sys.argv[1], 'sup')
		cp_subtitle_files(sys.argv[1], 'vtt')
	# Otherwise default to my Data directory
	else:
		cp_subtitle_files('./Data' 'ass')
		cp_subtitle_files('./Data' 'smi')
		cp_subtitle_files('./Data' 'srt')
		cp_subtitle_files('./Data' 'ssa')
		cp_subtitle_files('./Data' 'str')
		cp_subtitle_files('./Data' 'sup')
		cp_subtitle_files('./Data' 'vtt')