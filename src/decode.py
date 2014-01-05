import base64
import os
import sys
import argparse
from argparse import ArgumentParser

"""qtb64id - Quick terminal Base64 image decoder
functions:
	validfile: (...)
    argparser: (...)
    imgdecode:
        info - encoded base64 include file info?
               example: "data:image/jpeg;base64,"
        inputfile - path to encoded file.
"""

# Checking if file exist
#def validfile(parser, arg):
#	if not os.path.exists(arg):
#		parser.error("The file %s does not exist!"%arg)
#	else:
#		return open(arg,'r')

# Parsing arguments
# -i: filename
# -c: filetest (if file contains info about image)
# -t: filetype 
def argparser():
	global args
	parser = argparse.ArgumentParser(
						description="qtb64id - Quick terminal Base64 image decoder")
	parser.add_argument("-i", dest="filename", required=True,
    					help="Input file with encoded base64 string", metavar="FILE",
    					#type=lambda x: validfile(parser,x)
    					)
	parser.add_argument("-c", dest="filetest", required=False,
						help="(y/n) Input if string in file contain info (ex.: \"data:image/jpeg;base64,\"")
	parser.add_argument("-t", dest="filetype", required=False,
						help="Input file type (ex.: \"jpg\", \"png\", etc.)")

	args = parser.parse_args()


# Silly switch for filetype
def filetypec():
	global fext
	if args.filetype == "jpg":
		fext = ".jpg"
	elif args.filetype == "png":
		fext = ".png"
	else:
		print("wtf")
	return fext

# Main function for decoding image
def imgdecode(info, inputfile):
	if info == "y":
		pass
	if info == "n":
		filetypec()

	encoded_b64 = open(inputfile, "rb").read()
	imgdata = base64.b64decode(encoded_b64)
	file_name = os.path.splitext(inputfile)
	fname = file_name[0]

	imgFile = open(fname + fext, "wb")
	imgFile.write(imgdata)

	print("done!")

# Running program
def main():
	argparser()
	imgdecode(args.filetest, args.filename)

main()