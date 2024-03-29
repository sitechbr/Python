# socket: создание сетевых приложений

Библиотека socket в Python позволяет создавать сетевые приложения, работать с протоколами TCP, UDP и др. Она предоставляет дос1туп к сокетам, которые являются конечной точкой двухсторонней связи между клиентом и сервером.

В библиотеке socket есть несколько функций для работы с сокетами, основные из них:

    - socket(): создает новый сокет и возвращает его дескриптор.
    - bind(): связывает сокет с определенным адресом.
    - listen(): прослушивает входящие соединения на сокете.
    - accept(): принимает входящее соединение.
    - connect(): устанавливает соединение с другим сокетом.
    - send(): отправляет данные через сокет.
    - recv(): принимает данные из сокета.

Пример создания TCP-сервера:

```python
import socket

HOST = '0.0.0.0' # Используем все доступные интерфейсы
PORT = 9002 # Произвольный порт

# Создание сокета
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()  # Слушаем новые подключения

    print(f"Server is listening on {HOST}:{PORT}...")

    while True:
        conn, addr = s.accept()  # Принимаем новое подключение
        with conn:
            print(f"Connected by {addr}")

            while True:
                data = conn.recv(1024)  # Получаем сообщение от клиента
                if not data:  # Если сообщение пустое, то закрываем соединение
                    print(f"Client {addr} closed the connection")
                    break

                message = data.decode().strip()  # Декодируем полученное сообщение
                print(f"Received message from {addr}: {message}")

                response = message + message  # Формируем ответ, умножив полученное сообщение на 2

                conn.sendall(response.encode())  # Отправляем ответ клиенту
```
В этом коде мы создаем объект socket с использованием AF_INET для указания IPv4 и SOCK_STREAM для указания, что мы хотим использовать TCP-соединение. Затем мы привязываем сокет к IP-адресу и порту и начинаем прослушивание сокета.

Когда клиент подключается, мы принимаем его соединение и ждем сообщения от него. Когда мы получаем сообщение, мы добавляем двойную строку и отправляем его обратно клиенту.

Мы продолжаем принимать сообщения от клиента до тех пор, пока он не отправит сообщение или exit. Затем мы закрываем соединение и закрываем сокеты.

Пример создания TCP-клиента:
```python
import socket

HOST = '127.0.0.1'  # адрес сервера
PORT = 9002  # порт сервера

# создаем сокет
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # устанавливаем соединение с сервером
    s.connect((HOST, PORT))
    print('Connected to server')

    # запрашиваем у пользователя ввод сообщений, пока он не введет "exit"
    while True:
        message = input('Enter message: ')
        if message == 'exit':
            break

        # отправляем сообщение серверу
        s.sendall(message.encode())

        # получаем ответ от сервера и выводим его на экран
        data = s.recv(1024)
        print('Received:', data.decode())
```

В этом примере мы используем бесконечный цикл, который запрашивает у пользователя ввод сообщений до тех пор, пока он не введет «exit». Затем мы отправляем сообщение на сервер и получаем ответ.
