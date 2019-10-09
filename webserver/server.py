#import socket module
from socket import *
import sys # In order to terminate the program
FILE_PATH = 'C:/Users/tude/Project/CompuerNetworkHomework/webserver/data/'
serverSocket = socket(AF_INET, SOCK_STREAM)
#Prepare a sever socket
#Fill in start
serverSocket.bind(('localhost', 80))
serverSocket.listen(1)
#Fill in end
while True:
    #Establish the connection
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()
    try:
        message = connectionSocket.recv(1024).decode().split('\r\n')[0]
        filename = message.split()[1]
        print(FILE_PATH + filename[1:])
        f = open(FILE_PATH + filename[1:], encoding='UTF-8')     
        outputdata = f.read()
        #Send one HTTP header line into socket
        #Fill in start
        connectionSocket.send('HTTP/1.1 200 OK\r\n'.encode())
        connectionSocket.send('Content-type: text/html; charset=UTF-8\r\n\r\n'.encode())
        #Fill in end
        #Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())
        
        connectionSocket.close()
    except IOError as e:
        #Send response message for file not found
        #Fill in start
        connectionSocket.send('HTTP/1.1 404 Not Found\r\n'.encode())
        connectionSocket.send('Content-type: text/html; charset=UTF-8\r\n\r\n'.encode())
        connectionSocket.send('404 Not Found\r\n'.encode())
        #Fill in end
        #Close client socket
        #Fill in start
        connectionSocket.close()
        #Fill in end            
serverSocket.close()
sys.exit()#Terminate the program after sending the corresponding data   
