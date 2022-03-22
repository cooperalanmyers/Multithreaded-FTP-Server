# Multithreaded FTP Server
# 3/19/31

import socket
import struct
import random

server_ip = 'localhost'
server_port = 2309
buffer_size = 1024
new_server_port = random.randint(0,9999)

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def connect():
    print ("CONNECT <server name/IP address> <server port>")
    connectionData =  input()

    separator = ' '
    connectTemp = connectionData.split(separator, -1)

    paramOne = 'CONNECT'
    connectIP = connectTemp[1]
    connectPort = connectTemp[2]


    if connectTemp[0] == paramOne:
        client_socket.connect((connectIP, connectPort))

def list_files():
    
    new_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    new_client_socket.bind((server_ip, new_server_port))

    new_client_socket.listen()
    
    print ("Searching for list of files..\n")
    
    try:
        client_socket.send("LIST")
    except:
        print ("Server error upon request.")
        return

    try:
        # Recieving number of files
        num_files = struct.unpack("i", client_socket.recv(4))[0]
    
        for i in range(int(num_files))
            file_name_size = struct.unpack("i", client_socket.recv(4))[0]
            file_name = client_socket.recv(file_name_size)
            file_size = struct.unpack("i", client_socket.recv(4))[0]
            print "\t{} - {}b".format(file_name, file_size)
            client_socket.send("1")
            
        total_size = struct.unpack("i", s.recv(4))[0]
    
    except:
        print ("Couldn't retrieve listing")
        return

    try:
        # Final check
        s.send("1")
        return

    except:
        print ("Couldn't get final server confirmation")
        return

def quit():
    client_socket.send("QUIT")

    client_socket.recv(BUFFER_SIZE)
    client_socket.close()
    print "Server connection ended"
    return

connect()


print ("\n\nWelcome to the FTP client.
        \n\nCall one of the following functions:
        \nCONNECT           : Connect to server
        \nLIST              : List files
        \nRETR              : Retrieve file
        \nSTOR              : Send file
        \nQUIT              : Exit\n")

while True:

    # Listen for a command
    prompt = input("\nEnter a command: ")
       
    if prompt[:7].upper() == "CONNECT":
        connect()

    elif prompt[:4].upper() == "LIST":
        list_files()

    elif prompt[:4].upper() == "RETR":
        retrieve_file()

    elif prompt[:4].upper() == "STOR":
        store_file()

    elif prompt[:4].upper() == "QUIT":
        quit()
        break

    else:
        print "Command not recognised; please try again"

client_socket.close()
