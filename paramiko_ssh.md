# paramiko: работа с SSH-протоколоd

Библиотека paramiko — это Python-библиотека, которая предоставляет функциональность для работы с SSH-протоколом и управления удаленными серверами.

SSH (Secure Shell) — это протокол безопасной удаленной работы с устройствами по сети. Он позволяет аутентифицироваться на удаленном сервере и выполнять команды в командной строке, необходимые для управления сервером.

Библиотека paramiko позволяет подключаться к удаленному серверу по SSH-протоколу, аутентифицироваться на нем, выполнять команды и обмениваться данными между локальной машиной и удаленным сервером. Она обеспечивает удобный и простой интерфейс для работы с SSH-протоколом.

Некоторые возможности, которые предоставляет библиотека paramiko:

    - Аутентификация по паролю или по ключу SSH.
    - Запуск команд на удаленном сервере и получение результатов выполнения.
    - Отправка и получение файлов между локальной машиной и удаленным сервером.
    - Управление удаленным сервером через SFTP.
    - Работа с SSH-туннелями.
    - Поддержка протоколов SSHv2 и SFTPv3.

Выполнение команд

Пример подключения к удаленному серверу и выполнения команды:
```python
import paramiko

# Создание объекта SSHClient
ssh = paramiko.SSHClient()

# Установка политики автоматического подключения
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# Подключение к серверу по SSH
ssh.connect('192.168.1.1', username='user', password='password')

# Выполнение команды на удаленном сервере
stdin, stdout, stderr = ssh.exec_command('ls -l')

# Получение вывода команды
print(stdout.read().decode())

# Закрытие соединения
ssh.close()
```

В данном примере создается объект SSHClient и устанавливается политика автоматического подключения. Затем происходит подключение к удаленному серверу по SSH-протоколу с использованием имени пользователя и пароля. После этого выполняется команда ls -l на удаленном сервере и выводится ее результат.
Управление файлами

Для работы с SFTP в библиотеке paramiko есть класс SFTPClient. Пример загрузки файла на удаленный сервер:

```python
import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname='server_ip', username='username', password='password')

sftp = ssh.open_sftp()
local_path = '/path/to/local/file' #Путь к файлу на вашем устройстве
remote_path = '/path/to/remote/file' #Путь к файлу на сервере
sftp.put(local_path, remote_path)
sftp.close()
ssh.close()

Для загрузки файла с удалённого сервера на ваше устройство, достаточно заменить строку

sftp.put(local_path, remote_path) на sftp.get(remote_path, local_path) 

```

SSH-туннели

SSH-туннель (или SSH-проброс) — это механизм, который позволяет обеспечить безопасную связь между двумя удаленными узлами через ненадежный сетевой канал. Это достигается путем создания шифрованного туннеля между двумя хостами, в котором весь трафик, проходящий через этот туннель, шифруется и защищен от перехвата.

Примеры использования:

    Проброс локального порта на удаленный хост:

```python
import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('remote_host', username='user', password='passwd')

transport = ssh.get_transport()
transport.request_port_forward('127.0.0.1', 2222)

ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command('ls -l /tmp')
print(ssh_stdout.read())
```
В этом примере мы создаем SSH-подключение к удаленному хосту и пробрасываем локальный порт 2222 на удаленный хост. После этого мы выполняем команду ls -l /tmp на удаленном хосте через созданный туннель и выводим результат.

    Проброс удаленного порта на локальный хост:
```python 
import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('remote_host', username='user', password='passwd')

transport = ssh.get_transport()
transport.request_port_forward('0.0.0.0', 2222, remote_address=('remote_host', 22))

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect('localhost', username='user', password='passwd', port=2222)

stdin, stdout, stderr = client.exec_command('ls -l /tmp')
print(stdout.read())
```
В этом примере мы создаем SSH-подключение к удаленному хосту и пробрасываем удаленный порт 22 на локальный хост на порт 2222. Затем мы создаем новое SSH-подключение к локальному хосту через созданный туннель и выполняем команду ls -l /tmp на удаленном хосте через созданный туннель.

SSH-туннель может быть полезен в пентесте для обхода ограничений безопасности, связанных с защитой сетевых ресурсов.

Например, если имеется удаленный сервер, на котором запущено приложение, к которому нужно получить доступ, но доступ к этому серверу ограничен сетевой политикой, можно использовать SSH-туннель для установления безопасного канала связи между локальной машиной и удаленным сервером. Таким образом, можно обойти ограничения на доступ к ресурсу и получить к нему доступ через SSH-туннель.

SSH-туннели также могут использоваться для обхода блокировки сетевых портов, например, для доступа к сетевому сервису, который был заблокирован администратором сети.
