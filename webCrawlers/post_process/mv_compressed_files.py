import glob
import os
import fnmatch
import shutil
import sys

def iterFindFiles(path, fnexp):
	for root, dirs, files in os.walk(path):
		for filename in fnamtch.filter(files, fnexp):
			yield os.path.join(root, filename)

iii = 0
for fileName in iterFindFiles(r"./input", "*.zip"):
	iii = iii + 1
	newFileName = "zip/" + str(i) + "_" + os.path.basename(fileName)
	print(fileName + " <===> " + newFileName)
	shutil.move(fileName, newFileName)

iii = 0
for fileName in iterFindFiles(r"./input", "*.rar"):
	iii = iii + 1
	newFileName = "rar/" + str(i) + "_" + os.path.basename(fileName)
	print(fileName + " <===> " + newFileName)
	shutil.move(fileName, newFileName)

iii = 0
for fileName in iterFindFiles(r"./input", "*.7z"):
	iii = iii + 1
	newFileName = "7z/" + str(i) + "_" + os.path.basename(fileName)
	print(fileName + " <===> " + newFileName)
	shutil.move(fileName, newFileName)