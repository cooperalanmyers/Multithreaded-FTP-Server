# Multithreaded FTP  Server
# 3/33/21

import socket
import threading
import ftplib


print "\nFTP server is running.\n\nTo begin, connect a client."

def functionOne(connection_socket):
    sentence = connection_socket.recv(buffer_size).decode('utf-8')
    modified_sentence = sentence.upper()
    connection_socket.send(modified_sentence.encode('utf-8'))
    connection_socket.close()

server_ip = 'localhost'
server_port = 2309
buffer_size = 1024

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((server_ip, server_port))

server_socket.listen()

while True:
    connection_socket, addr = server_socket.accept()
    threading.Thread(target=functionOne, args=(connection_socket,)).start()
    print ("Successfully connected to: \n" + addr)

def quit():
    # Send quit conformation
    connection_socket.send("1")
    # Close the server
    connection_socket.close()
    server_socket.close()

while True:

    print ("\n\nWaiting for instruction")
    data = connection_socket.recv(BUFFER_SIZE)
    print ("\nRecieved instruction: {}".format(data))

    if data == "CONNECT":
        upld()

    elif data == "LIST":
        list_files()

    elif data == "RETR":
        dwld()

    elif data == "STOR":
        delf()

    elif data == "QUIT":
        quit()

    # Reset the data to loop
    data = None

