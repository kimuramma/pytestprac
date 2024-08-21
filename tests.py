import rsa
import json

# Замените на ваш публичный ключ в формате PKCS1
public_key_str = "b'-----BEGIN RSA PUBLIC KEY-----'MIGJAoGBALvqofBRsZZaV7EXxvJk2BzubZd55jFz44VP+dKbEQ/vGR1u29BtrAjR542MJJ3seF5AS/8z02plCaw/VxzASscebYcWo9/U9VPyae25IUZHMYngX6nsLVIj8OiLvgGjrKur9TfOa3nNjkkiO5c7vi1oWtW/9xIZD/J95CvQ/bCdAgMBAAE='-----END PUBLIC KEY-----"

# Загрузите публичный ключ
public_key = rsa.PublicKey.load_pkcs1(public_key_str.encode(), format='PEM')

# Ваши данные
data = {
   "iin":"900101300451",
   "mobile_phone":"+77778889900",
   "lang":"ru",
   "theme":"dark"
}

# Преобразуйте данные в строку JSON
data_str = json.dumps(data)

# Зашифруйте данные
encrypted_data = rsa.encrypt(data_str.encode(), public_key)

# Получите зашифрованные данные в шестнадцатеричном формате
encrypted_data_hex = encrypted_data.hex()

print("Зашифрованные данные:", encrypted_data_hex)
