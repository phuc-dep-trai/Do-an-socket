#client.py
from os import system
import send_email
import pop_1

Username = "Hong Phuc <test@gmail.com>"
PASS = "ahihi"
MailServer = "127.0.0.1"
smtp = 2225
pop3 = 3335
Autoload = 10
k = 1
while k!= 0: 
    print("Vui lòng chọn menu: ")
    print("1. Để gửi email")
    print("2. Để xem danh sách các email đã nhận")
    print("0. thoat")
    # k = input("Bạn chọn: ")
    k = int(input("Bạn chọn: "))
    if k==1:
        # gửi tới email
        print("Đây là thông tin soạn email: (nếu không điền vui lòng nhấn enter bỏ qua)")
        #nhập nơi gửi tới
        To = input("To: ").split(',')
        CC = input("CC: ").split(',')
        BCC = input("BCC: ").split(',')
    
        #nội dung
        Subject = input("Subject: ")
        Content = input("Content: ")
        file_path = []
        #gửi file
        choose = int(input("có gửi kèm file(1. có,2. không): "))
        if choose == 1:
            num = int(input("cho biết số lượng file muốn gửi: "))
            for i in range(1,num+1):
                tam = input("cho biết đường dẫn file thứ "+str(i)+": ")
                file_path.append(tam)
        send_email.send_mail(MailServer,smtp,Content,Username,To,CC,BCC,Subject,file_path)
        print("\n\nĐã gửi email thanh công\n\n")