import sqlite3
def Filter(filename_):
    File_={}
    fileName = ['Project', 'Important', 'Work', 'Spam']
    Type = ['From', 'Subject', 'Content', 'Spam']
    for Part in fileName:
        File_[f'{Part}'] ={}
        for part in Type:
            File_[f'{Part}'][f'{part}'] = []


    # Kết nối đến cơ sở dữ liệu
    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()

    # Đọc nội dung từ file SQL và thực hiện
    with open(f'{filename_}', 'r') as file:
        sql_script = file.read()
        cursor.executescript(sql_script)

    # Thực hiện truy vấn SQL để lấy dữ liệu
    cursor.execute("SELECT * FROM FilterRules")

    # Lấy kết quả
    results = cursor.fetchall()

    # In ra màn hình theo định dạng mong muốn
    for result in results:
        condition_type = result[1]
        conditions = result[2]
        target_folder = result[3]
        
        File_[f'{target_folder}'][f'{condition_type}'] = conditions.split(', ')
    return File_
    # Đóng kết nối
    conn.close()

Filter('filter.sql')
