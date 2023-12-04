import math
from msilib.schema import File
from os import system
import re
import os
from socket import *

#---------------------------------PROJECT--------------------------------#
Project = {}
Project['From'] = ['duyphuc2425@gmail.com']
Project['Subject'] = []
Project['Content'] = []
#---------------------------------IMPORT---------------------------------#
Import = {}
Import['From'] = []
Import['Subject']=['dd']
Import['Content'] = []
#--------------------------------WORK-----------------------------------#
Work = {}
Work['From'] = []
Work['Subject'] = []
Work['Content'] = ['xin chao']
#--------------------------------Spam------------------------------------#
Spam = {}
Spam['From'] = []
Spam['Subject'] = ['thu']
Spam['Content'] = ['thu']

#------------------------Hàm xem có file đính kèm không-----------------#
def _xu_ly_(SOCKET, NAME,CONTENT):
#----------------------------------------------FROM------------------------------------------------------------#
    PATTERN  = r'From:(\w+)'
    pattern = re.compile(r'From: (.*)\r')
    match = re.search(pattern, CONTENT)
    if match:
        From = match.group(1)
        From = From.split('<')
        if len(From) > 1:
            From = From[1].split('>')
    else:
        print("EROR")
    if From[0] in Project['From']:
        FILE("C:\\Users\\duyph\\OneDrive\\Desktop\\Socket\\client\\test@gmail.com\\Project\\", NAME, CONTENT)
    elif From[0] in Import['From']:
        FILE("C:\\Users\\duyph\\OneDrive\\Desktop\\Socket\\client\\test@gmail.com\\Important\\", NAME, CONTENT)
    elif From[0] in Work['From']:
        FILE("C:\\Users\\duyph\\OneDrive\\Desktop\\Socket\\client\\test@gmail.com\\Work\\", NAME, CONTENT)
    elif From[0] in Spam['From']:
        FILE("C:\\Users\\duyph\\OneDrive\\Desktop\\Socket\\client\\test@gmail.com\\Spam\\", NAME, CONTENT)
#-------------------------------------------------Subject-----------------------------------------------------#
    PATTERN = r'Subject:(\w+)'
    pattern = re.compile(r'Subject: (.*)\r')
    match = re.search(pattern,CONTENT)
    Subject =''
    if match:
        Subject = match.group(1)
    else:
        print("EROR")
    if kiem_tra_chuoi(Subject, Project['Subject']):
        FILE("C:\\Users\\duyph\\OneDrive\\Desktop\\Socket\\client\\test@gmail.com\\Project\\", NAME, CONTENT)
    elif kiem_tra_chuoi(Subject, Import['Subject']):
        FILE("C:\\Users\\duyph\\OneDrive\\Desktop\\Socket\\client\\test@gmail.com\\Important\\", NAME, CONTENT)
    elif kiem_tra_chuoi(Subject, Work['Subject']):
        FILE("C:\\Users\\duyph\\OneDrive\\Desktop\\Socket\\client\\test@gmail.com\\Work\\", NAME, CONTENT)
    elif kiem_tra_chuoi(Subject, Spam['Subject']):
        FILE("C:\\Users\\duyph\\OneDrive\\Desktop\\Socket\\client\\test@gmail.com\\Spam\\", NAME, CONTENT)
        
#-------------------------------------------------CONTENT-----------------------------------------------------#

    PATTERN     =       f'Content-Type: multipart/mixed; boundary="([^"]+)"'
    match       =       re.search(PATTERN             , CONTENT)
    if match:
        boundary = "--"+ match.group(1)
        Content = CONTENT.split(boundary)
        for i in range(0,len(Content)):
            Content[i] = Content[i].split('\r\n')
#------------------------------------------------SEND CONTENT-------------------------------------------------#
        for i in range(2,len(Content[2])):
            noidung = Content[2][i]
            if noidung != '':
                if kiem_tra_chuoi(noidung,Project['Content']):
                     FILE("C:\\Users\\duyph\\OneDrive\\Desktop\\Socket\\client\\test@gmail.com\\Project\\", NAME, CONTENT)
                elif kiem_tra_chuoi(noidung,Import['Content']):
                    FILE("C:\\Users\\duyph\\OneDrive\\Desktop\\Socket\\client\\test@gmail.com\\Important\\", NAME, CONTENT)
                elif kiem_tra_chuoi(noidung,Work['Content']):
                    FILE("C:\\Users\\duyph\\OneDrive\\Desktop\\Socket\\client\\test@gmail.com\\Work\\", NAME, CONTENT)
                elif kiem_tra_chuoi(noidung,Spam['Content']):
                    FILE("C:\\Users\\duyph\\OneDrive\\Desktop\\Socket\\client\\test@gmail.com\\Spam\\", NAME, CONTENT)
    else:
        Content = CONTENT.split('\r\n')
    system('pause')

#----------------------------------------FUNCTION-------------------------------------#
def kiem_tra_chuoi(chuoi, mang_kiem_tra):
    for tu_khoa in mang_kiem_tra:
        if tu_khoa.lower() in chuoi.lower():
            return True
    return False

#FUNCTION SEND
def SEND_COMMAND(SOCKET,COMMAND,CHOOSE):        #function send to email server
    COMMAND     +=  '\r\n'                      #    
    SOCKET.send(COMMAND.encode())               #
    RES          =   RECV_DATA(SOCKET)          #
    RES          =   RES.decode()               #
    if CHOOSE:                                  #condition to print result
        print(RES)
    return RES
        
    
    
#FUNCTION RECV
def RECV_DATA(SOCKET):
    DATA         =   b''                        #
    while True:                                 #
        CHUNK    =   SOCKET.recv(1024)          #
        if not CHUNK:                           #
            break                               #
        DATA     +=  CHUNK                      #
        if b'\r\n' in DATA:                     #
            break                               #
    return DATA                                 #

#FUNCTION UIDL
def UIDL(MSG):
    MSG = MSG.split('\r\n')
    for i in range(1,len(MSG)-2):
        MSG[i] = MSG[i].split(' ')
    return MSG

#SAVER FILE
def FILE(file_path, name_file, msg):
    file_path += name_file + '.txt'
    with open(file_path, 'w') as file:
        file.write(msg)

#RETURN LIST FILE NAME
def _LI_FILE_NAM_(FOLDER_PATH):
    # Lấy danh sách tên file trong thư mục
    file_names = os.listdir(FOLDER_PATH)
    return file_names

#--------------------------------------MAIN----------------------------------------------------#
HOST            =       '127.0.0.1'
PORT            =        3335

with socket(AF_INET,         SOCK_STREAM)    as         CLIENT:
    SERVER_ADD  = (HOST,     PORT)
    CLIENT.connect(SERVER_ADD)
    RECV_DATA(CLIENT)
    
    SEND_COMMAND(CLIENT,'CAPA'                          , False)
    SEND_COMMAND(CLIENT, 'USER duyphuc2425@gmail.com'   , False)
    SEND_COMMAND(CLIENT, 'PASS 12312323'                , False)
    SEND_COMMAND(CLIENT, 'STAT'                         , False)
    SEND_COMMAND(CLIENT, 'LIST'                         , False)
    MSG = SEND_COMMAND(CLIENT, 'UIDL'                   , False)
    MSG = UIDL(MSG)
    num = 0
    file_names = _LI_FILE_NAM_("C:\\Users\\duyph\\OneDrive\\Desktop\\Socket\\client\\test@gmail.com\\inbox\\")
    for i in range(1,len(MSG) - 2):
        check = True
        for j in range(0,len(file_names)):
            if((MSG[i][1]+'.txt') == file_names[j]):
                check = False
        if check:
            CONTENT = SEND_COMMAND(CLIENT,f'RETR {int(MSG[i][0])}', False)
            FILE('C:\\Users\\duyph\\OneDrive\\Desktop\\Socket\\client\\test@gmail.com\\inbox\\',MSG[i][1], CONTENT)
            _xu_ly_(CLIENT,MSG[i][1],CONTENT)
    
    SEND_COMMAND(CLIENT, 'QUIT'                         , False)