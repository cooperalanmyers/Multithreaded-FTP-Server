# Multithreaded FTP  Server
# 3/23/31
# Cooper Myers
# CIS 457 Data Communications

import socket
import threading
import sys
import os
import struct
import time

# Method for Server Instruction Commands Menu
def command_menu(connection_socket):
    while True:
           print ("\n\nWaiting for instruction")
           data = connection_socket.recv(BUFFER_SIZE).decode('utf-8')
      
           # Print Requested Command to Screen
           print ("\nRecieved instruction: {}".format(data))
    
           # If Command Matches go to Following Helper Method
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
    # connection_socket.close()
    return

def list_files():
    print ("Listing files...")
    # Get list of files in directory

    listing = os.listdir(os.getcwd())
    # Send over the file names
    for i in listing:
        # File name
        connection_socket.send(i.encode('utf-8'))

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


def dataConnection():
    new_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    new_server_socket.connect()

# Beginning Message to Server
print ("\nFTP server is running.\n\nTo begin, connect a client.\n")

# Storing Server Data Information
server_ip = 'localhost'
server_port = 9000
BUFFER_SIZE = 1024

# Creating Server Socket, Binding, then Listening
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((server_ip, server_port))

server_socket.listen()
print("The Server is ready to recieve!")


while True:
    connection_socket, addr = server_socket.accept()
    threading.Thread(target=command_menu, args=(connection_socket,)).start()
