from multiprocessing.connection import Client
from os import system
import socket
import re
import sys

def send_command(socket, command):
    # Send the command over the socket
    socket.send(command.encode())
    response = receive_data(socket)
    print(response.decode())
    return response.decode()

def receive_data(sock):
    data = b""
    while True:
        chunk = sock.recv(1024)
        if not chunk:
            break
        data += chunk
        if b'\r\n' in data:
            break
    return data

def _fsdf_():
    HOST = '127.0.0.1'
    PORT = 3335  # Change this to the correct POP3 port
    server_add = (HOST, PORT)
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(server_add)
    client.send(f"CAPA\r\n".encode())
    client.recv(1024)
    response = receive_data(client)
    print(response.decode())
    # Send POP3 commands
    send_command(client, "USER duyphuc2425@gmail.com\r\n")
    send_command(client, "PASS 12334542\r\n")
    stat_command = 'STAT\r\n'
    client.send(stat_command.encode())
    response = client.recv(1024).decode()
    response = response.split(' ')
    send_command(client, "LIST\r\n")
    # for i in range(1,int(match[1]) + 1):
    #     send_command(client, f"DELE {i}\r\n")
    send_command(client, "UIDL\r\n")
    # for i in range(1,int(response[1]) + 1):
    #     client.send(f"DELE {i}\r\n".encode())
    #     recv1 =  client.recv(1024)
    #     print(recv1.decode())
    while response != "QUIT":
        response = input()
        send_command(client,f"{response}\r\n")

    client.close()

_fsdf_()




