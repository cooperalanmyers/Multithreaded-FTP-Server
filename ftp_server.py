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
               return
        
           elif (type(data) == int) & len(data) == 4:
                global(new_port_number = data)
                '''new_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                new_server_socket.connect((server_ip, int(new_port_number)))
                print("New Port Number is stored!\nPORT: " + new_port_number)
                
                newData = "Now Connected!"
                new_server_socket.send(newData.encode('utf-8'))'''
                
           # Reset Data to Loop Through Again
           data = None
    
def quit():
    # Close the server
    connection_socket.close()
    print("Successfully disconnected from client")
    return

def list_files():
    print("Listing files now!\n")
    
    new_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    print(new_port_number)
    
    time.sleep(3)
    
    new_server_socket.connect((server_ip, int(new_port_number)))
    
    files = [f for f in os.listdir('.') if os.path.isfile(f)]
    temp = ""
    
    for f in files:
        temp = temp + f + "\n"
        print(temp)
    
    new_server_socket.send(temp.encode('utf-8'))
    new_server_socket.close()
    return

def retr():
      return

def stor():
      return

"""
def dataConnection():
    return
    # new_server_socket.connect((server_ip, int(new_port_number)))
    # new_server_socket.connect((server_ip, int(new_port_number)))

    #newData = "Now Connected!"
    #new_server_socket.send(newData.encode('utf-8'))
"""
    

# Beginning Message to Server
print ("\nFTP server is running.\n\nTo begin, connect a client.\n")

# Storing Server Data Information
server_ip = 'localhost'
server_port = 2309
BUFFER_SIZE = 1024

# Creating Server Socket, Binding, then Listening
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((server_ip, server_port))

server_socket.listen()
print("The Server is ready to recieve!")


while True:
    connection_socket, addr = server_socket.accept()
    threading.Thread(target=command_menu, args=(connection_socket,)).start()
