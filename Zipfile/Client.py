# import necessary modules
import os
import socket
import tqdm


# assigning HOST and PORT Number of the server
HOST = "127.0.0.1"
PORT = 65432


# assign buffer_size as 1024 bits per Second
BUFFER_SIZE = 1024
SEPARATOR = "<SEPARATOR>"


# get the name of the file which we want to send to the server
filename = input("Enter name of the file to be sent: ")
# get the file size 
filesize = os.path.getsize(filename)


# create a TCP client socket 
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
	# connect to the intended server 
	print(f"[+] Connecting to {HOST}:{PORT}")
	client_socket.connect((HOST, PORT))
	print("[+] Connected")
	#send the filename and file size to the server
	client_socket.send(f"{filename}{SEPARATOR}{filesize}".encode())
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