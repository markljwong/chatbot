import glob
import os
import fnmatch
import shutil
import sys

def iterfindfiles(path, fnexp):
	for root, dirs, files in os.walk(path):
		for filename in fnmatch.filter(files, fnexp):
			yield os.path.join(root, filename)

iii = 0
for filename in iterfindfiles(r"./input/", "*.lrc"):
	iii = iii + 1 
	newfilename = "lrc/" + str(iii) + "_" + os.path.basename(filename)
	print filename + " <===> " + newfilename
	shutil.move(filename, newfilename)

iii = 0
for filename in iterfindfiles(r"./input/", "*.ass"):
	iii = iii + 1 
	newfilename = "ass/" + str(iii) + "_" + os.path.basename(filename)
	print filename + " <===> " + newfilename
	shutil.move(filename, newfilename)

iii = 0
for filename in iterfindfiles(r"./input/", "*.smi"):
	iii = iii + 1 
	newfilename = "smi/" + str(iii) + "_" + os.path.basename(filename)
	print filename + " <===> " + newfilename
	shutil.move(filename, newfilename)

iii = 0
for filename in iterfindfiles(r"./input/", "*.srt"):
	iii = iii + 1 
	newfilename = "srt/" + str(iii) + "_" + os.path.basename(filename)
	print filename + " <===> " + newfilename
	shutil.move(filename, newfilename)

iii = 0
for filename in iterfindfiles(r"./input/", "*.ssa"):
	iii = iii + 1 
	newfilename = "ssa/" + str(iii) + "_" + os.path.basename(filename)
	print filename + " <===> " + newfilename
	shutil.move(filename, newfilename)

iii = 0
for filename in iterfindfiles(r"./input/", "*.str"):
	iii = iii + 1 
	newfilename = "str/" + str(iii) + "_" + os.path.basename(filename)
	print filename + " <===> " + newfilename
	shutil.move(filename, newfilename)

iii = 0
for filename in iterfindfiles(r"./input/", "*.sup"):
	iii = iii + 1 
	newfilename = "sup/" + str(iii) + "_" + os.path.basename(filename)
	print filename + " <===> " + newfilename
	shutil.move(filename, newfilename)

iii = 0
for filename in iterfindfiles(r"./input/", "*.vtt"):
	iii = iii + 1 
	newfilename = "vtt/" + str(iii) + "_" + os.path.basename(filename)
	print filename + " <===> " + newfilename
	shutil.move(filename, newfilename)

iii = 0
for filename in iterfindfiles(r"./input/", "*.vtt"):
	iii = iii + 1 
	newfilename = "vtt/" + str(iii) + "_" + os.path.basename(filename)
	print filename + " <===> " + newfilename
	shutil.move(filename, newfilename)
