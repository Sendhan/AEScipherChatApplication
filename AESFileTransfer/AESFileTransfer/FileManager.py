# import necessary modules
import os
import subprocess
import shutil


# import necessary user defined modules
import CompressionDecompression as CD
import EncryptDecrypt as ED
import CheckSumValidator as CSV


def getDefaultDir():
	return os.getcwd()
	
	
def getHometDir():
	homedir = os.environ['HOME']
	return homedir
	
	
def MakeNewDirectory(platform_num):
	path = os.environ['HOME']
	if platform_num == 1:
		path = path + r'\Documents\AESFileTransfer'
		os.mkdir(path)
		return path
	elif platform_num == 3:
		path = path + r'/Documents/AESFileTransfer'
		os.mkdir(path)
		return path 
		

def changeDirectory(path):
	os.chdir(path)
	

def transferFile(path):
	default_dir = os.getcwd()
	target = r'/Users/macbook/Desktop/AESSendFiles'
	os.mkdir(target)
	file_names = os.listdir(path)
	filelist = []
	for file_name in file_names:
		print(f"file_name: {file_name}")
		opt = input("Do you want to transfer the above file? ")
		if opt == "yes":
			shutil.move(os.path.join(path, file_name), target)
			filelist.append(file_name)
	filename = input("Enter the name of the file: ")	
	os.chdir(target)
	CD.Compress(filename, filelist)
	os.chdir(default_dir)
	return filename
	
	
def collectfiles(path):
	file_names = os.listdir(path)
	target = r'/Users/macbook/Desktop/AESFileTransfer'
	filelist = []
	for file_name in file_names:
		print(f"file_name: {file_name}")
		opt = input("Do you want to transfer the above file? ")
		if opt == "yes":
			filelist.append(file_name)
	ZipFileName = input("Enter the name of the file(Zipfile): ")
	ZipFileNamepath = target+r'/'+ZipFileName
	print(f"ZipFile path: {ZipFileNamepath}")
	CD.Compress(ZipFileNamepath, filelist)
	print(f"ZipFileName: {ZipFileName}")
	return ZipFileName
	
	
def receivefile(path, filename, key):
	changeDirectory(path)
	data = ED.decrypt(key, filename)
	filename = filename[:len(filename)-4]
	with open(filename, 'wb') as file:
		file.write(data)
	CD.Decompress(filename)
	receiver_checksum = CSV.getCheckSum(filename)
	print("receivefile :", filename)
	return receiver_checksum