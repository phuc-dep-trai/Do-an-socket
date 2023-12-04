#POP3
from multiprocessing.connection import Client
import socket
from urllib import response

def send_command(sock, command):
    sock.send(command.encode("utf-8"))
    response = sock.recv(1024)
    print(response.decode("uft-8"))

def _POP3_():
    client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client.connect('127.0.0.1',3335)
    
    response = client.recv(1024)
    print(response.decode("uft-8"))
    
    #xac thuc
    send_command(Client,"CAPA")
    send_command(Client,"USER test@gmail.com")
    send_command(client,"PASS 12334542")
    #lay danh sach thu
    send_command(client,"LIST\r\n")
    #Lay noi dung thu
    send_command(client,"RETE 1\r\n")
    client.close()    

