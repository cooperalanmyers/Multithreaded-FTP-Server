# Multithreaded FTP Server
# 3/23/31
# Cooper Myers
# CIS 457 Data Communications

import socket
import struct
import random

server_ip = 'localhost'
server_port = 2309
buffer_size = 1024

# Creating Client Socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect Method From Client Input
def connect():
    print ("CONNECT <server name/IP address> <server port>")
    connectionData =  input()

    separator = ' '
    connectTemp = connectionData.split(separator, -1)

    paramOne = 'CONNECT'
    connectIP = '127.0.0.1' if connectTemp[1] == 'localhost' else connectTemp[1]
    connectPort = connectTemp[2]

    # If Client Says "CONNECT" Then Connect
    if connectTemp[0].upper() == paramOne: 
        client_socket.connect((connectIP, int(connectPort)))
        client_socket.send(paramOne.encode('utf-8'))

def list_files():
    listMessage = "LIST"
    client_socket.send(listMessage.encode('utf-8'))
    print ("Searching for list of files..\n")

    # Helper Method For New Data Connection
    dataConnection()
    
    try:
        # Recieving number of files
        num_files = struct.unpack("i", client_socket.recv(4))[0]
    
        for i in range(int(num_files)):
            file_name_size = struct.unpack("i", client_socket.recv(4))[0]
            file_name = client_socket.recv(file_name_size)
            file_size = struct.unpack("i", client_socket.recv(4))[0]
            print("\t{} - {}b".format(file_name, file_size))
            client_socket.send("1")
            
        total_size = struct.unpack("i", s.recv(4))[0]
    
    except:
        print ("Couldn't retrieve listing")
        return

    try:
        # Final check
        client_socket.send("1")
        return

    except:
        print ("Couldn't get final server confirmation")
        return

def retr():
    pass

def quit():
    quitMessage = "QUIT"
    client_socket.send(quitMessage.encode('utf-8'))
    #client_socket.close()
    print ("Server connection ended")
    return

def dataConnection():
    new_server_port = random.randint(0,9999)

    new_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    new_client_socket.bind((server_ip, new_server_port))

    new_client_socket.listen()

    ## client_socket.send(new_server_port.encode('utf-8'))



# Anything Below is the Client Menu that Automatically Prompts


print ("""\n\nWelcome to the FTP client.
        \n\nCall one of the following functions:
        \nCONNECT           : Connect to server
        \nLIST              : List files
        \nRETR              : Retrieve file
        \nSTOR              : Send file
        \nQUIT              : Exit\n""")

while True:

    # Listen for a command
    prompt = input("\nEnter a command: ")
       
    if prompt[:7].upper() == "CONNECT":
        connect()

    elif prompt[:4].upper() == "LIST":
        list_files()

    elif prompt[:4].upper() == "RETR":
        retr()

    elif prompt[:4].upper() == "STOR":
        store_file()

    elif prompt[:4].upper() == "QUIT":
        quit()
        break
    
    #if isinstance(var, int)''


    else:
        print ("Command not recognized; please try again")
