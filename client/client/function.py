import secrets
import string

def get_content_transfer_encoding(input_string):
        # Kiểm tra xem chuỗi có chứa ký tự nằm ngoài phạm vi ASCII hay không
    ascii_chars = all(ord(char) < 128 for char in input_string)

    # Kiểm tra xem chuỗi có chứa ký tự từ bảng mã mở rộng (ISO-8859-1) hay không
    iso_8859_1_chars = all(32 <= ord(char) <= 255 for char in input_string)

    # Kiểm tra xem chuỗi có chứa ký tự không thuộc bảng mã ISO-8859-1 hay không
    utf8_chars = all(ord(char) <= 255 for char in input_string)

    if ascii_chars:
        return "ASCII"
    elif iso_8859_1_chars:
        return "ISO-8859-1 (Extended ASCII)"
    elif utf8_chars:
        return "UTF-8 (Unicode)"
    else:
        return "Không xác định"
    
def generate_random_string(length = 24):
    alphabet = string.ascii_letters + string.digits
    return ''.join(secrets.choice(alphabet) for _ in range(length))
