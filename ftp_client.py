# Multithreaded FTP Server
# 3/19/31

import socket


server_ip = 'localhost'
server_port = 2309
buffer_size = 1024

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
