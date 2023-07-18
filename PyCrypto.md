# PyCrypto: работа с шифрованием

PyCrypto — это библиотека для работы с криптографией на языке Python, которая позволяет шифровать и дешифровать данные, а также работать с хэш-функциями и генерировать случайные числа. Она содержит множество алгоритмов шифрования и хэширования, таких как AES, RSA, DES, SHA-1, SHA-256 и другие.

Для начала работы с PyCrypto необходимо установить библиотеку. Это можно сделать, выполнив следующую команду в командной строке: `pip3 install pycryptodome`
Пример шифрования данных с помощью AES:
```python 
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

data = b'secret data'

key = get_random_bytes(16)
cipher = AES.new(key, AES.MODE_EAX)
ciphertext, tag = cipher.encrypt_and_digest(data)

print(f'До шифрования: {data}')
print(f'После шифрования: {ciphertext}')
print(f'Тег: {tag}')
```

Переменная tag в данном коде содержит аутентификационный тег (authentication tag), который представляет собой короткую строку байт, используемую для проверки подлинности данных и защиты от подделок. Этот тег рассчитывается на основе открытого текста и ключа шифрования и включается вместе с зашифрованными данными.
```┌──(kali㉿kali)-[~]
└─$ python3 test.py  
Before encoding: b'secret data'
After encoding: b'\xc9\x8d\x8fYCI`\xb6u\x18\xf8'
Tag: b'\xd7\xdc\x1b-s\xa6\x93\xd2xS\x8e\xfe\x88\x1c}K'
```
Шифрование с помощью RSA:

Следующий код шифрует часть данных для получателя в файл encrypted_data.bin, для которого у нас есть открытый ключ RSA. Открытый ключ RSA хранится в файле с именем pubkey.pem Поскольку мы хотим иметь возможность шифровать произвольный объем данных, мы используем гибридную схему шифрования. Мы используем RSA с PKCS#1 OAEP для асимметричного шифрования сеансового ключа AES. Затем сеансовый ключ можно использовать для шифрования всех фактических данных.
```python
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP

data = "Этот текст будет зашифрован с помощью RSA".encode("utf-8")
file_out = open("encrypted_data.bin", "wb")

recipient_key = RSA.import_key(open("pubkey.pem").read())
session_key = get_random_bytes(16)

# Шифрование сеансового ключа открытым ключом RSA
cipher_rsa = PKCS1_OAEP.new(recipient_key)
enc_session_key = cipher_rsa.encrypt(session_key)

# Шифрование данных с помощью сеансового ключа AES
cipher_aes = AES.new(session_key, AES.MODE_EAX)
ciphertext, tag = cipher_aes.encrypt_and_digest(data)
[ file_out.write(x) for x in (enc_session_key, cipher_aes.nonce, tag, ciphertext) ]
file_out.close()
```
Получатель имеет закрытый ключ RSA. Он будет использовать его для расшифровки сеансового ключа, а вместе с ним и остальной части файла:
```python
from Crypto.PublicKey import RSA
from Crypto.Cipher import AES, PKCS1_OAEP

file_in = open("encrypted_data.bin", "rb")

private_key = RSA.import_key(open("private.pem").read())

enc_session_key, nonce, tag, ciphertext = \
   [ file_in.read(x) for x in (private_key.size_in_bytes(), 16, 16, -1) ]
file_in.close()

# Decrypt the session key with the private RSA key
cipher_rsa = PKCS1_OAEP.new(private_key)
session_key = cipher_rsa.decrypt(enc_session_key)

# Decrypt the data with the AES session key
cipher_aes = AES.new(session_key, AES.MODE_EAX, nonce)
data = cipher_aes.decrypt_and_verify(ciphertext, tag)
print(data.decode("utf-8"))
```
