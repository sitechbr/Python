# requests: HTTP-запросы
HTTP (Hypertext Transfer Protocol) — это протокол передачи гипертекста, который используется для передачи данных между веб-сервером и веб-браузером. В Python для работы с HTTP-запросами и ответами используется модуль requests.
Установить модуль requests можно с помощью pip: pip3 install requests
После установки библиотеки можно выполнять запросы. Наиболее распространенными являются GET и POST запросы.   
Пример GET запроса:
```
import requests

response = requests.get('https://www.google.com/')
print(response.status_code)
print(response.text)
```



В данном примере выполняется GET запрос на сайт google.com. В ответ мы получаем статус-код (200, если запрос прошел успешно) и содержимое страницы в виде текста.   
Пример POST запроса:
```
import requests

data = {'key1': 'value1', 'key2': 'value2'}
response = requests.post('https://httpbin.org/post', data=data)
print(response.status_code)
print(response.text)
```

В данном примере выполняется POST запрос на сайт httpbin.org, который является тестовым сайтом для проверки работы HTTP-запросов. В ответ мы получаем статус-код и содержимое страницы в виде JSON-объекта, который содержит переданные в POST запросе данные.
```
┌──(kali㉿kali)-[~]
└─$ python3 test.py       
200
{
  "args": {}, 
  "data": "", 
  "files": {}, 
  "form": {
    "key1": "value1", 
    "key2": "value2"
  }, 
  "headers": {
    "Accept": "*/*", 
    "Accept-Encoding": "gzip, deflate, br", 
    "Content-Length": "23", 
    "Content-Type": "application/x-www-form-urlencoded", 
    "Host": "httpbin.org", 
    "User-Agent": "python-requests/2.28.1", 
    "X-Amzn-Trace-Id": "Root=1-643e501b-5efe99f270b32a05588a947c"
  }, 
  "json": null, 
  "origin": "Ваш внешний IP адрес", 
  "url": "https://httpbin.org/post"
}
```


В запросах также можно указывать заголовки (headers), параметры (params), cookies и многое другое.

Например, можно выполнить GET запрос с заголовком:

```
import requests

headers = {'User-Agent': 'Mozilla/5.0'}
response = requests.get('https://www.google.com/', headers=headers)
print(response.status_code)
print(response.text)
```

В данном примере мы указываем заголовок User-Agent, который говорит серверу, что мы используем браузер Mozilla/5.0. Без указания этого заголовка Google будет возвращать страницу, оптимизированную для мобильных устройств.   

При работе с запросами также необходимо учитывать возможность ошибок и обрабатывать их при помощи исключений:

```import requests

try:
    response = requests.get('https://www.google.com/')
    response.raise_for_status()
    print(response.status_code)
    print(response.text)
except requests.exceptions.HTTPError as err:
    print(err)
```
В данном примере мы выполняем GET запрос и обрабатываем возможную ошибку при помощи исключения HTTPError. Если запрос завершится с ошибкой, то будет выведено сообщение с описанием ошибки.   

Также можно задавать параметры запроса в URL, например:
```
import requests

params = {'q': 'python'}
response = requests.get('https://www.google.com/search', params=params)
print(response.url)
print(response.status_code)
```

В ответ мы получим URL https://www.google.com/search?q=python и статус ответа

Кроме этого, библиотека requests предоставляет возможность автоматической сериализации и десериализации данных в различных форматах, таких как JSON, XML, YAML, CSV и другие.

Например, для отправки POST-запроса с данными в формате JSON, необходимо воспользоваться методом requests.post() и передать нужные параметры в аргументе data в формате словаря. Для указания заголовков запроса, можно использовать аргумент headers.
```
import requests

url = "https://google.com"
data = {"name": "John", "age": 30}
headers = {"Content-type": "application/json"}

response = requests.post(url, json=data, headers=headers)

if response.status_code == 200:
    print(response.json())
else:
    print("Error:", response.status_code)

```
