# import necessary modules
import os
import socket
import tqdm
from zipfile import ZipFile


# IMPORT necessary USER defined modules
import FileManager as fm 
import EncryptDecrypt as ED
import CheckSumValidator as CSV  


key = b'\xa2\xe8\xc3?\x0b}\xb6\xd4\xc1ZgN\x9a?zw'

path = input("Enter the path of the files to be sent: ")
file_name = fm.collectfiles(path)
sender_checksum = CSV.getCheckSum(file_name)


# assigning HOST and PORT Number of the server
HOST = "127.0.0.1"
PORT = 65432


# assign buffer_size as 1024 bits per Second
BUFFER_SIZE = 1024
SEPARATOR = "<SEPARATOR>"


with open(file_name, 'rb') as file:
	data = file.read()
filename = file_name + ".bin"
ED.encrypt(key, data, filename)


# get the name of the file which we want to send to the server
# filename = file_name input("Enter name of the file to be sent: ")
# get the file size 
filesize = os.path.getsize(filename)


# create a TCP client socket 
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
	# connect to the intended server 
	print(f"[+] Connecting to {HOST}:{PORT}")
	client_socket.connect((HOST, PORT))
	print("[+] Connected")
	#send the filename and file size to the server
	client_socket.send(f"{filename}{SEPARATOR}{filesize}{SEPARATOR}{sender_checksum}".encode())
	# start sending the file
	progress = tqdm.tqdm(range(filesize), f"Sending {filename}", unit="B", unit_scale=True, unit_divisor=1024)
	with open(filename, 'rb') as file:
		while True:
			# read the bytes from the file
			bytes_read = file.read(BUFFER_SIZE)
			if not bytes_read:
				# file transmitting is done
				break
			# we use sendall to assure transmission in busy networks
			client_socket.sendall(bytes_read)
			# update the progress bar
			progress.update(len(bytes_read))
			
			
os.remove(filename)
os.remove(file_name)