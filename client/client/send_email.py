#sendall_emmail


import datetime
import email.utils
from email import message
from functools import total_ordering
from http import client
import imp
import math
from multiprocessing.connection import Client
import socket
import base64
import ssl
import uuid
from datetime import date, datetime
import os
import re
from function import *
import time

def send_mail(host,port,msg,from_1,To_1,CC,BCC,subject,file_path):

    endmsg = "\r\n.\r\n"
    mailserver = (host,port)
    clientSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    
    clientSocket.connect(mailserver)


    recv = clientSocket.recv(1024).decode()
    if recv[:3] != '220':
        print('220 reply not received from server.')
    
    heloCommand = f'EHLO [{host}]\r\n'
    clientSocket.sendall(heloCommand.encode())
    recv1 = clientSocket.recv(1024).decode()
    if recv1[:3] !='250':
        print('250 reply not received from server.')

    #from
    mailFrom = f"MAIL FROM:<{from_1}>\r\n"
    clientSocket.sendall(mailFrom.encode())
    recv2 = clientSocket.recv(1024)


    #TO
    for part in To_1:
        if(part != ""):
            rcptTo = f"RCPT TO:<{part}>\r\n"
            clientSocket.sendall(rcptTo.encode())
            recv3 = clientSocket.recv(1024)
    
    #CC 
    if CC[0]!="":
        for part in CC:
            if(part != ""):
                clientSocket.sendall(f"RCPT TO:<{part}>\r\n".encode())
                recv3 = clientSocket.recv(1024)
    #BCC
    if (BCC[0] != ""):
        for part in BCC:
            if(part != ""):
                clientSocket.sendall(f"RCPT TO:<{part}>\r\n".encode())
                recv3 = clientSocket.recv(1024)
    #---------------------------------------DATA-----------------------
    data = "DATA\r\n"
    clientSocket.sendall(data.encode())
    recv4 = clientSocket.recv(1024)
    # ------------------- CONTENT HEADERS -----------------------------
    ID = str(uuid.uuid4())
    #content-Type
    if (len(file_path) !=0 ):
        # Mã hóa Base64
        
        boundary = f"------------{generate_random_string()}"   
        content_type = f"Content-Type: multipart/mixed; boundary=\"{boundary}\"\r\n"
        clientSocket.sendall(content_type.encode())
     
    #Message-ID
    ID = str(uuid.uuid4())
    message_id = f"Message-ID: <{ID}@gmail.com>\r\n"
    clientSocket.sendall(message_id.encode())

    #Date time
    current_data = email.utils.formatdate(localtime=True)
    date_1 =f"Date: {current_data}\r\n" 
    clientSocket.sendall(date_1.encode())

    #MIME-Version: 1.0
    mine_version = "MIME-Version: 1.0\r\n"
    clientSocket.sendall(mine_version.encode())

    #User_agent.
    user_agent = "User-Agent: Mozilla Thunderbird\r\n"
    clientSocket.sendall(user_agent.encode())

    #content-laguage
    content_laguage = "Content-Language: vi-x-KieuCu.[Chuan]\r\n"
    clientSocket.sendall(content_laguage.encode())    

    #TO
    if To_1[0] != "":
        sendall_To = f"To: "
        i = 0
        for part in To_1:
            i = i + 1
            sendall_To += part
            if i != len(To_1):
                sendall_To += ','        
        sendall_To += "\r\n"
        clientSocket.sendall(sendall_To.encode())
    #CC
    if CC[0] != "":
        sendall_CC = f"CC: "
        i = 0
        for part in CC:
            i = i + 1
            sendall_CC += part
            if i != len(CC):
                sendall_CC += ','        
        sendall_CC += "\r\n"
        clientSocket.sendall(sendall_CC.encode())
    #from
    from_2 = f"From: {from_1}\r\n"
    clientSocket.sendall(from_2.encode())

    # subject
    email_subject = f"Subject: {subject}\r\n"
    clientSocket.sendall(email_subject.encode())

    #text
    if (len(file_path) != 0):
        text1 = f"\r\nThis is a multi-part message in MIME format.\r\n--{boundary}\r\n"
        clientSocket.sendall(text1.encode())

    #Content-Type
    content_type1 = f"Content-Type: text/plain; charset=UTF-8; format=flowed\r\n"
    clientSocket.sendall(content_type1.encode()) 

    #content-Tranfer-Encoding
    if get_content_transfer_encoding(str(msg)) == str("ASCII"):
        content_transfer_encoding =  7
    else :
        content_transfer_encoding =  8
    
    CTE = f"Content-Transfer-Encoding: {content_transfer_encoding}bit\r\n"
    clientSocket.sendall(CTE.encode())   
    #---------------------------------------------------------------------------------------------------------------------------------------------------
    clientSocket.sendall(f"\r\n{msg}\r\n".encode())
    
     # Đính kèm file

    for part in file_path:
        if part != "":
            clientSocket.sendall(("\r\n--" +boundary + "\r\n").encode())
            filename = os.path.basename(part)
            attachment_content = open(part, 'rb').read()
            attachment_base64 = base64.b64encode(attachment_content).decode()
            file_extension = os.path.splitext(part)[1][1:];
            duoi = filename.split('.')[-1]
            if duoi == 'txt':
                clientSocket.sendall(f'Content-Type: text/plain; charset=UTF-8; name="{filename}"\r\n'.encode())
            else:
                clientSocket.sendall(f'Content-Type: application/{duoi}; charset=UTF-8; name="{filename}"\r\n'.encode())
            clientSocket.sendall(f'Content-Disposition: attachment; filename="{filename}"\r\nContent-Transfer-Encoding: base64\r\n\r\n'.encode())
            chunk_size = 72          
            total_size = len(attachment_base64)
            offset = 0
            while offset <total_size:
                chunk = attachment_base64[offset:offset + chunk_size] +'\r\n'
                offset += chunk_size
                try:
                    abc= clientSocket.send(chunk.encode())
                except ConnectionError as e:
                    print(f"Error sending data: {e}")
                    break 
            clientSocket.sendall(b'\r\n \r\n') 
            
#C:\Users\duyph\OneDrive\Desktop\234324.pdf

    if(len(file_path) != 0):
        clientSocket.sendall(("--"+boundary + "--").encode())
    
    # end_sendallallmail( sendallall".")
    clientSocket.sendall(endmsg.encode())
    recv_msg = clientSocket.recv(1024)
    recv5 = "QUIT\r\n"
    clientSocket.sendall(recv5.encode())
    clientSocket.recv(1024)
    #exit program
    clientSocket.close()
