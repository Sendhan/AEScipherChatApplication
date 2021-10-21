# import necessary modules
import os
import socket
import tqdm
import time


# importing user defined modules
import ApplicationOpener as AppO


# assigning HOST and PORT Number
HOST = "127.0.0.1"
PORT = 65432


# assign buffer_size as 1024 bits per Second
BUFFER_SIZE = 1024
SEPARATOR = "<SEPARATOR>"


# create a tcp server socket as s
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	# bind the socket to the local ip address
	s.bind((HOST, PORT))
	# listen for incoming connections from the client
	s.listen(5)
	print(f"[+] Listening as {HOST}:{PORT}")
	# accept the connection from the client
	client_socket, address = s.accept()
	# print the address of the connected client
	print(f"[+] {address} is connected")
	# receive the filename and file size from the client
	received = client_socket.recv(BUFFER_SIZE).decode()
	filename, filesize = received.split(SEPARATOR)
	# remove absolute path if there is
	filename = os.path.basename(filename)
	# convert the file-size from strings to integer
	filesize = int(filesize)
	# start receiving the file from the client
	progress = tqdm.tqdm(range(filesize), f"Received {filename}", unit="B", unit_scale=True, unit_divisor=1024)
	with open("new"+filename, 'wb') as file:
		while True:
			# read 1024 bytes from the socket (receive)
			bytes_read = client_socket.recv(BUFFER_SIZE)
			if not bytes_read:    
				# nothing is received
				# file transmitting is done
				break
			# write to the file the bytes we just received
			file.write(bytes_read)
			# update the progress bar
			progress.update(len(bytes_read))


# finds the Operating System used for the server
platform_num = AppO.find_platform()
# opens the file with the given default application
print("Opening", "new"+filename, "...")
time.sleep(5)
AppO.open_application(platform_num, "new"+filename) 
# print the data present in the file in the console(like terminal or Command Prompt)
AppO.open_console(filename)