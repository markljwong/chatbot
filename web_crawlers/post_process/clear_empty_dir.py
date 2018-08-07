import glob
import os
import fnmatch
import shutil
import sys

def clearEmptyDir(path, fnexp):
	for root, dirs, files in os.walk(path):
		if 0 == len(files) and len(dirs) == 0:
			print(root)
			os.rmdir(root)

clearEmptyDir(r"./extracted/", "")
clearEmptyDir(r"./sorted/", "")