import glob
import os
import fnmatch
import shutil
import sys

def iterFindFiles(path, fnexp):
	for root, dirs, files in os.walk(path):