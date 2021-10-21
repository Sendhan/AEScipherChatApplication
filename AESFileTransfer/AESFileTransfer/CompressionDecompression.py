# import necessary modules
from zipfile import ZipFile
import os


def Compress(ZipFileName, filelist):
	with ZipFile(ZipFileName, 'w') as zf:
		for file in filelist:
			zf.write(file)
			
def Decompress(ZipFileName):
	with ZipFile(ZipFileName, 'r') as zf:
		zf.extractall()
		
