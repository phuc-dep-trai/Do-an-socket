from re import sub
import send_email 
import tkinter as tk
from tkinter import ttk 


host = "127.0.0.1"
port = 2225

def box():
    def send_button_clicked():
        subject = subject_entry.get()
        from1 = from1_entry.get()
        to1 = to1_entry.get()
        body = body_text.get("1.0",tk.END)
        send_email.send_mail(host,port,body,from1,To_1= [to1],CC=[],BCC=[], subject=subject,file_path="null")
    #Tạo một cửa số và các thành phần GUI
    root = tk.Tk()
    root.title("Send Email")

    #Nhan va on nhap chu de
    subject_label = tk.Label(root,text="Chủ đề: ")
    subject_label.grid(row=0, column=0,sticky='w')

    subject_entry = tk.Entry(root, width=30)
    subject_entry.grid(row=0,column=0)

    #nhan va on ten nguoi gui
    from_label = tk.Label(root,text="From:")
    from_label.grid(row=1,column=0,sticky='w')

    default_from_entry = "test@gmail.com"
    from1_entry = tk.Entry(root,width=30)
    from1_entry.insert(0,default_from_entry)
    from1_entry.grid(row=1, column=0)

    #nhan va o ten nguoi nhan
    to1_label = tk.Label(root,text="To: ")
    to1_label.grid(row=2, column=0, sticky='w')

    default_to = "test@gmail.com"
    to1_entry = tk.Entry(root,width=30)
    to1_entry.insert(0,default_to)
    to1_entry.grid(row=2, column=0)

    # Nhãn và ô nhập cho nội dung
    body_label = tk.Label(root, text="Nội dung:")
    body_label.grid(row=3, column=0, sticky='w')

    # Sử dụng Text widget và thiết lập giá trị mặc định
    default_body_content = "Nội dung"
    body_text = tk.Text(root, height=10, width=40)
    body_text.insert("1.0", default_body_content)  # Chèn nội dung mặc định
    body_text.grid(row=4, column=0, sticky='e')

    # Nút Gửi
    send_button = tk.Button(root, text="Gửi", command=send_button_clicked)
    send_button.grid()

    # Chạy ứng dụng
    root.mainloop()

box()