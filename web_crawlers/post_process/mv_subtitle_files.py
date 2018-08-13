import os
import shutil
import sys

def mv_subtitle_files(data_dir, filetype):
	counter = 0

	full_data_dir =Path(data_dir).resolve()
	input_dir = os.path.join(full_data_dir, 'extracted')
	output_dir = os.path.join(full_data_dir, "sorted")
	filetype_dir = os.path.join(output_dir, fileType)

	if not os.path.isdir(output_dir):
		os.makedirs(output_dir)
	if not os.path.isdir(filetype_dir):
		os.makedirs(filetype_dir)

	# Iterate through input directory and move applicable files to the new directory
	for root, dirs, files in os.walk(input_dir):
		for file in files:
			if file.endswith(filetype):
				print(file)
				shutil.movefile(os.path.join(root, file), os.path.join(filetype_dir, file))
				counter += 1

	if counter > 0:
		print("-------------------------")
		print("[INFO}\tFound in: " + input_dir + " : " + str(counter) + " files\n")

if __name__ == '__main__':
	# If user gives input, use that as Data directory
	if len(sys.argv) == 2:
		mv_subtitle_files(sys.argv[1], 'ass')
		mv_subtitle_files(sys.argv[1], 'lrc')
		mv_subtitle_files(sys.argv[1], 'smi')
		mv_subtitle_files(sys.argv[1], 'srt')
		mv_subtitle_files(sys.argv[1], 'ssa')
		mv_subtitle_files(sys.argv[1], 'str')
		mv_subtitle_files(sys.argv[1], 'sup')
		mv_subtitle_files(sys.argv[1], 'vtt')
	# Otherwise default to my Data directory
	else:
		mv_subtitle_files('.\Data', 'ass')
		mv_subtitle_files('.\Data', 'smi')
		mv_subtitle_files('.\Data', 'srt')
		mv_subtitle_files('.\Data', 'ssa')
		mv_subtitle_files('.\Data', 'str')
		mv_subtitle_files('.\Data', 'sup')
		mv_subtitle_files('.\Data', 'vtt')