from socket import *

serverName = '127.0.0.1' #localhost
serverPort = 12000

clientSocket = socket(AF_INET,SOCK_DGRAM)
message = input('Ingresa texto en minusculas: ')
clientSocket.sendto(message.encode(),(serverName,serverPort))
modifiedMessage,serverAddress = clientSocket.recvfrom(2048)
print(modifiedMessage.decode())
clientSocket.close()
