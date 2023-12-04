import sqlite3

def General(file_):
    File ={}
# Kết nối đến cơ sở dữ liệu SQLite và thực hiện truy vấn
    conn = sqlite3.connect(':memory:')  # Sử dụng cơ sở dữ liệu trong bộ nhớ
    cursor = conn.cursor()
    with open(file_,'r') as file:
        sql_script = file.read()
        cursor.executescript(sql_script)
    # Thực hiện truy vấn để lấy dữ liệu từ bảng Config
    cursor.execute("SELECT * FROM Config")
    rows = cursor.fetchall()
    # In ra màn hình dữ liệu theo định dạng yêu cầu
    for row in rows:
        setting_name = row[1]
        setting_value  =row[2]
        File[f'{setting_name}'] = setting_value
    return File
    # Đóng kết nối
    conn.close()
a = General('config.sql')
print(a)