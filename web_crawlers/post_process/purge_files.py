import glob
import os
import fnmatch
import shutil
import sys

def purgeFiles(path, fnexp):
	for root, dirs, files in os.walk(path):
		for fileName in fnmatch.filter(files, fnexp):
			yield os.path.join(root, fileName)

for suffix in ("*.mp4", "*.txt", "*.JPG", "*.htm", "*.doc", "*.docx", "*.nfo", "*.sub", "*.idx"):
	for filename in purgeFiles(r"./sorted/", suffix):
		print(fileName)
		os.remove(fileName)