# Multithreaded FTP Server
# 3/23/31
# Cooper Myers
# CIS 457 Data Communications

import socket
import struct
import random
import time

server_ip = 'localhost'
server_port = 2309
buffer_size = 1024
new_server_port = random.randint(2000,9999)
new_server_port = str(new_server_port)
# Make sure I am using credible port numbers within a range

# Creating Client Socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

new_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

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
        
        time.sleep(3)
        
        client_socket.send(new_server_port.encode('utf-8'))
        
        #newData = client_socket.recv(buffer_size).decode('utf-8')
        #print(newData)
    
def list_files():
    listMessage = "LIST"
    
    # client_socket.connect(('localhost', 2309))
    client_socket.send(listMessage.encode('utf-8'))
    client_socket.send(str(new_server_port).encode('utf-8'))

    time.sleep(2)
 
    # new_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    new_client_socket.bind((server_ip, int(new_server_port)))
    new_client_socket.listen()
    
    temp.sleep(3)
    
    # new_client_socket.accept()
    connection_socket, addr = new_client_socket.accept()
    # new_client_socket.accept()

    time.sleep(3)

    grab_files(connection_socket)
    
    connection_socket.close()
    new_client_socket.close()
    return
    
    # Helper Method For New Data Connection
    # dataConnection()
    
def grab_files():
    newDataForFiles = new_client_socket.recv(buffer_size)
    print(newDataForFiles)
    return

def retr():
    pass

def quit():
    quitMessage = "QUIT"
    client_socket.send(quitMessage.encode('utf-8'))
    #client_socket.close()
    print ("Server connection ended")
    return

def new_port_check():
    portMessage = "PORT"
    client_socket.send(portMessage.encode('utf-8'))


"""
def dataConnection():
    # new_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    new_client_socket.bind((server_ip, int(new_server_port)))

    new_client_socket.listen()
    
    # new_client_socket.accept()
    connection_socket, addr = new_client_socket.accept()

    
    newData = new_client_socket.recv(buffer_size)
    # recieve!!!!
    print(newData)
    
    # newData = "Client as Server Connected"
    # new_client_socket.send(newData.encode('utf-8'))
"""


# Anything Below is the Client Menu that Automatically Prompts


print ("""\n\nWelcome to the FTP client.
        \n\nCall one of the following functions:
        \nCONNECT           : Connect to server
        \nLIST              : List files
        \nRETR              : Retrieve file
        \nSTOR              : Send file
        \nPORT              : New Port Name
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

    elif prompt[:4].upper() == "PORT":
        new_port_check()
        
    elif prompt[:4].upper() == "QUIT":
        quit()
    
    #if isinstance(var, int)''


    else:
        print ("Command not recognized; please try again")
