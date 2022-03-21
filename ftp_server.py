# Multithreaded FTP  Server
# 3/33/21

import socket
import threading
import sys
import os
import struct
import time


print ("\nFTP server is running.\n\nTo begin, connect a client.")

server_ip = 'localhost'
server_port = 2309
buffer_size = 1024

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((server_ip, server_port))

server_socket.listen()
    

def quit():
    # Send quit conformation
    connection_socket.send("1")
    # Close the server
    connection_socket.close()
    server_socket.close()

def list_files():
    print ("Listing files...")
    # Get list of files in directory
    listing = os.listdir(os.getcwd())
    # Send over the file names
    for i in listing:
        # File name
        connection_socket.send(i)
        # Make sure that the client and server are syncronised
        connection_socket.recv(BUFFER_SIZE)

    #Final check
    connection_socket.recv(BUFFER_SIZE)
    print ("Successfully sent file listing")
    connection_socket.close()
    return


while True:

    connection_socket, addr = server_socket.accept()
    threading.Thread(target=None, args=(connection_socket,)).start()

    print ("\n\nWaiting for instruction")
    data = connection_socket.recv(BUFFER_SIZE)
    print ("\nRecieved instruction: {}".format(data))

    if data == "LIST":
        list_files()

    elif data == "RETR":
        retr()

    elif data == "STOR":
        stor()

    elif data == "QUIT":
        quit()

    # Reset the data to loop
    data = None

