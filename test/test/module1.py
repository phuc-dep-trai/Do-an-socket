import secrets
import string

st = "Swg7Tf73KSq0toJ0V0JM89Lz"

def generate_random_string(length = 24):
    alphabet = string.ascii_letters + string.digits
    return ''.join(secrets.choice(alphabet) for _ in range(length))

random_string = generate_random_string(24)  # Thay 24 bằng độ dài mong muốn
print(random_string)
