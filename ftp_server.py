# Multithreaded FTP  Server
# 3/33/21

import socket
import threading
import sys
import os
import struct
import time

# Beginning Message to Server
print ("\nFTP server is running.\n\nTo begin, connect a client.\n")

# Storing Server Data Information
server_ip = 'localhost'
server_port = 2309
buffer_size = 1024

# Creating Server Socket, Binding, then Listening
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((server_ip, server_port))

server_socket.listen()
print("The Server is ready to recieve!\")
    
# Method for Server Instruction Commands Menu
def command_menu():
    while true:
           print ("\n\nWaiting for instruction")
           data = connection_socket.recv(BUFFER_SIZE)
      
           # Print Requested Command to Screen
           print ("\nRecieved instruction: {}".format(data))
    
           # Helper Method using Target for commands
           if data == "LIST":
           list_files()

           elif data == "RETR":
           retr()

           elif data == "STOR":
           stor()

           elif data == "QUIT":
           quit()

           # Reset Data to Loop Through Again
           data = None
    
def quit():
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
      
def retr():
      return

def stor():
      return


while True:
    connection_socket, addr = server_socket.accept()
    threading.Thread(target=command_menu, args=(connection_socket,)).start()

