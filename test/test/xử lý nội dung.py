# # from email.parser import BytesParser
# # import email
# # import re

# # # Đoạn văn bản thư bạn nhận được
# # email_content = """
# # +OK 806
# # Content-Type: multipart/mixed; boundary="------------05a2bf1e-5a5d-4a4a-9b9d-2d3a6fe0ba7b"
# # Message-ID:<3061b788-47fa-4649-8751-e8db63106768@gmail.com>
# # Date: Fri, 17 Nov 2023 21:06:17 +0700
# # MiME-Version: 1.0
# # User-Agent: YourUserAgent/1.0
# # Content-Language: en-US
# # To: test@gmail.com
# # From: HongPhuc<HongPhuc@fit.edu.vn>
# # Subject: phuc

# # This is a multi-part message in MIME format.
# # ------------05a2bf1e-5a5d-4a4a-9b9d-2d3a6fe0ba7b
# #  text/plain; charset=UTF-8; format=flowed
# # Content-Transfer-Encoding: 7bit

# # 123456


# # ------------05a2bf1e-5a5d-4a4a-9b9d-2d3a6fe0ba7b
# # Content-Type: application/txt; name = text.txt
# # Content-Disposition: attachment; filename=text.txt
# # Content-Transfer-Encoding: base64

# # UGh1YyB4aW4gY2hhbyBtb2kgbmd1b2kgbmhh

# # ------------05a2bf1e-5a5d-4a4a-9b9d-2d3a6fe0ba7b
# # """

# # Your MIME-formatted string
# # mime_string = """
# # +OK 806
# # Content-Type: multipart/mixed; boundary="------------05a2bf1e-5a5d-4a4a-9b9d-2d3a6fe0ba7b"
# # Message-ID: <9694e7d9-16bc-4231-9668-0cf864ad8330@gmail.com>
# # Date: Sun, 19 Nov 2023 00:42:26 +0700
# # MiME-Version: 1.0
# # User-Agent: YourUserAgent/1.0
# # Content-Language: en-US
# # To: duyphuc2425@gmail.com
# # From: test@gmail.com
# # Subject: hello

# # This is a multi-part message in MIME format.
# # ------------36eb6fc0-802d-499e-bf6e-ec0a74a78f38
# # Content-Type: text/plain; charset=UTF-8; format=flowed
# # Content-Transfer-Encoding: 7bit

# # xin chao

# # ------------36eb6fc0-802d-499e-bf6e-ec0a74a78f38
# # Content-Type: application"txt"; name="text.txt"
# # Content-Disposition: attachment; filename="text.txt"
# # Content-Transfer-Encoding: base64

# # UGh1YyB4aW4gY2hhbyBtb2kgbmd1b2kgbmhh
 
# # ------------36eb6fc0-802d-499e-bf6e-ec0a74a78f38
# # """

# # #tim kiếm thứ mong muốn
# # pattern = re.compile(r'From: (.*)')
# # match = re.search(pattern, mime_string)

# # if match:
# #     message_id_value = match.group(1)
# #     print(message_id_value)
# # else:
# #     print("Message-ID not found.")


# #tìm kiếm boundary
# # #FUNCTION FIND BOUNDARY
# # def FIND_BOUNDARY(CONTENT):
# #     PATTERN     =       f'Content-Type: multipart/mixed; boundary="([^"]+)"'
# #     match       =       re.search(PATTERN             , CONTENT)
# #     if match:
        
# #         return match.group(1)
# #     else:
# #         return match
    
# # #FUNCTION CONTENT
# # def _CONTENT_ (CONTENT):
# #     BOUNARY = FIND_BOUNDARY(CONTENT)
    
# #     if BOUNARY:
# #         ARR = CONTENT.split(BOUNARY)
# #         for i in range(1,len(ARR)):


# # import os

# # # Đường dẫn đến thư mục bạn muốn kiểm tra
# # folder_path = "C:\\Users\\duyph\\OneDrive\\Desktop\\Socket\\client\\test@gmail.com\\Work\\"

# # # Lấy danh sách tên file trong thư mục
# # file_names = os.listdir(folder_path)

# # # In danh sách tên file
# # for file_name in file_names:
# #     print(file_name)


# # def kiem_tra_chuoi(chuoi, mang_kiem_tra):
# #     for tu_khoa in mang_kiem_tra:
# #         if tu_khoa.lower() in chuoi.lower():
# #             return True
# #     return False

# # # Ví dụ sử dụng hàm
# # chuoi_a = 'hello mọi người'
# # mang_chao = ['Hello', 'xin chao', 'Hi']
# # mang_person = ['Người', 'mọi', 'tốt']
# # mang_fruit = ['cam', 'Xoài', 'Quýt']

# # ket_qua_chao = kiem_tra_chuoi(chuoi_a, mang_chao)
# # ket_qua_person = kiem_tra_chuoi(chuoi_a, mang_person)
# # ket_qua_fruit = kiem_tra_chuoi(chuoi_a, mang_fruit)

# # print("Chuỗi có từ trong mảng chào không:", ket_qua_chao)
# # print("Chuỗi có từ trong mảng person không:", ket_qua_person)
# # print("Chuỗi có từ trong mảng fruit không:", ket_qua_fruit)


# import os
# import mimetypes
# import zipfile


# def open_file(file_path):
#     file_extension = os.path.splitext(file_path)[-1].lower()
    
#     if file_extension == ".zip":
#         open_zip(file_path)
#     else:
#         open_generic(file_path)

# def open_zip(file_path):
#     with zipfile.ZipFile(file_path, 'r') as zip_ref:
#         # In danh sách các file trong ZIP
#         print(f"Contents of {file_path}:\n{zip_ref.namelist()}\n")
        
#         # Trích xuất nội dung của một số file văn bản
#         for name in zip_ref.namelist():
#             if name.endswith(('.docx', '.pdf', '.txt')):
#                 with zip_ref.open(name) as file:
#                     content = file.read()
#                     print(f"Content of {name}:\n{content.decode()}\n")

# def open_generic(file_path):
#     mime_type, encoding = mimetypes.guess_type(file_path)
    
#     if mime_type:
#         if "pdf" in mime_type:
#             open_pdf(file_path)
#         elif "word" in mime_type:
#             open_docx(file_path)
#         elif "jpeg" in mime_type:
#             open_image(file_path)
#         else:
#             print(f"Unsupported file type: {mime_type}")
#     else:
#         print("Unable to determine file type.")

# def open_docx(file_path):
#     doc = Document(file_path)
#     text = "\n".join([paragraph.text for paragraph in doc.paragraphs])
#     print(f"Content of {file_path}:\n{text}\n")

# def open_pdf(file_path):
#     with open(file_path, 'rb') as file:
#         pdf_reader = PyPDF2.PdfFileReader(file)
#         num_pages = pdf_reader.numPages
#         text = ""
#         for page_num in range(num_pages):
#             page = pdf_reader.getPage(page_num)
#             text += page.extractText()
#         print(f"Content of {file_path}:\n{text}\n")

# def open_image(file_path):
#     img = Image.open(file_path)
#     img.show()

# # Thay đổi đường dẫn đến file bạn muốn mở
# fil


file_path = ["duongdan/text.txt"]