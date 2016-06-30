"""
Batch rename script
When you download numerous files at once, each having the same pattern in the filename that you want to get rid of, use this as as solution.

Python 2.7
How to use:
	python batch_rename.py "host dir" "phrase to replace" "replacing phrase"
"""

import os
import sys

def main(args):
	path 		= args[0]
	phrase 		= args[1]
	repPhrase 	= args[2]

	print "Scanning:",path
	print "files only with '"+phrase+"' to '"+repPhrase+"'"
	os.system(" ".join(["cd",path]))

	files = list()

	for i in os.listdir(path):
		if phrase in str(i):
			files.append(str(i))

	print "Matchings:",len(files)

	if len(files) != 0:
		for i in files:
			print "Renaming:",i
			before = str(path+"\\"+i).strip()
			after = str(path+"\\"+str(i).replace(phrase,repPhrase)).strip()
			os.rename(before,after)
	else:
		print "Error - No files to rename"

if __name__ == '__main__':
	main(sys.argv[1:])
