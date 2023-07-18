# BeautifulSoup: парсинг HTML-страниц

BeautifulSoup — это библиотека Python, которая предназначена для парсинга HTML-страниц. С её помощью можно извлекать данные из HTML-кода, например, тексты, ссылки, изображения, таблицы и многое другое. Библиотека умеет работать с различными типами парсера, включая встроенные в Python, а также с парсерами сторонних библиотек, таких как lxml.

Для начала работы с BeautifulSoup, необходимо установить его. Это можно сделать, выполнив команду в командной строке: `pip3 install beautifulsoup4`

После установки можно импортировать библиотеку и начать работу с HTML-кодом:

```python
import requests
from bs4 import BeautifulSoup

# URL страницы для парсинга
url = 'https://habr.com/ru/'

# Отправляем GET-запрос на указанный URL и сохраняем ответ в переменную response
response = requests.get(url)

# Преобразуем ответ в объект BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Находим все заголовки статей на странице и сохраняем их в переменную headers
headers = soup.find_all('a', {'class': 'tm-title__link'})

# Выводим заголовки всех статей
for header in headers:
    print(header.text)
```
В этом примере мы отправляем GET-запрос на главную страницу habr.com, затем создаем объект BeautifulSoup для обработки полученного HTML-кода. Далее мы находим все заголовки статей на странице и сохраняем их в переменную headers, а затем выводим их на экран.
```
┌──(kali㉿kali)-[~]
└─$ python3 test.py
УЦСБ и Positive Technologies успешно завершили внедрение PT Application Firewall в рамках импортозамещения
Игра на опережение
AI Doomism (ChatGPT & ИИ-истерия)
«Нанософт» 15 лет. От nanoCAD к инженерной экосистеме
Secure by Design: с чего начинается безопасность продукта
Преобразуем карты DOOM в SVG для лазерной резки
Рецепт установки ПОЛИНОМ:MDM под Linux
Голь на выдумки хитра или как сэкономить более 200 тыс.руб на изготовлении собственого оборудования
Клиент-серверное и межсервисное взаимодействие: разбираемся в REST, GraphQL, RPC и WebSocket
Встречаем сценарии умного дома Яндекса, которые сработают даже без интернета
Бионическая рука. Больше, чем  протез
«Прозрачный промоушн выгоден и разработчику, и его тимлиду». Нюансы карьеры разработчика на С++
Приложение для инженеров на Flutter
Гетерогенная распределенная система как способ миграции больших и не очень баз данных с MSSQL Server на PostgreSQL
Новое приложение Lemon8 от ByteDance рвет топы американского AppStore. Разбираемся, как оно устроено
Оптимизация настройки Webpack проекта на CRA
КПП в кармане: как мы автоматизировали контроль доступа на территорию с нуля
Добавляем SPDIF в легендарный Roland MT-32
Философские вопросы интернационализации веб-приложений
Vivaldi 6.0 — Пространство для творчества
```

Теперь рассмотрим более сложный пример, в котором мы будем парсить страницы с блогами на habr.com и извлекать оттуда название статьи, автора и дату публикации.

```python
import requests
from bs4 import BeautifulSoup

# URL страницы для парсинга
url = 'https://habr.com/ru/top/'

# Отправляем GET-запрос на указанный URL и сохраняем ответ в переменную response
response = requests.get(url)

# Преобразуем ответ в объект BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Находим все блоги на странице и сохраняем их в переменную blogs
blogs = soup.find_all('article', {'class': 'tm-articles-list__item'})

# Проходимся по каждому блогу и извлекаем название, автора и дату публикации
for blog in blogs:
    title = blog.find('a', {'class': 'tm-title__link'}).text.strip()
    author = blog.find('span', {'class': 'tm-user-info__user'}).text.strip()
    date = blog.find('span', {'class': 'tm-article-datetime-published'}).text.strip()

    # Выводим извлеченные данные на экран
    print(f'Название статьи: {title}\nАвтор: {author}\nДата публикации: {date}\n')
```
В этом коде мы сначала загружаем страницу с блогами на habr.com с помощью модуля requests, а затем используем модуль BeautifulSoup, чтобы распарсить HTML-код. Затем мы используем метод find_all, чтобы найти все статьи на странице с помощью тега article и его класса tm-articles-list__item.

Далее мы перебираем каждую статью и извлекаем из нее название, автора и дату публикации с помощью метода find и соответствующих тегов и классов. Метод text используется для извлечения текстового содержимого элементов, а метод strip — для удаления лишних пробелов и переносов строк.

Наконец, мы выводим извлеченные данные на экран, используя метод print.
```
┌──(kali㉿kali)-[~]
└─$ python3 test.py
Название статьи: Automation in mobile QA testing
Автор: AppQuantum
       16 hours ago
Дата публикации: 16 hours ago

Название статьи: Compiling fast .exe console applications with PHP 8.1, why not?
Автор: kovalensky
        Apr  8  at 13:19
Дата публикации: Apr  8  at 13:19

Название статьи: Langton's ant: a mystery cellular automaton
Автор: AKlimenkov
        Apr  1  at 12:31
Дата публикации: Apr  1  at 12:31

Название статьи: Array of weak in Swift
Автор: Leschev
        Apr  1  at 12:21
Дата публикации: Apr  1  at 12:21

Название статьи: GNU radio 802.11 black box optimization
Автор: VasyaPal
        Mar  31  at 22:10
Дата публикации: Mar  31  at 22:10

Название статьи: Not 'Doom' ported
Автор: quaer
        Mar  23  at 22:58
Дата публикации: Mar  23  at 22:58

Название статьи: About «free» #iam, #oidc, #saml, #etc
Автор: korkin25
        Mar  22  at 21:28
Дата публикации: Mar  22  at 21:28

Название статьи: The Collatz conjecture is the greatest math trick of all time
Автор: AKlimenkov
        Mar  21  at 18:13
Дата публикации: Mar  21  at 18:13

Название статьи: Tutorial. Onchain Analysis basics
Автор: pazlvbanke
        Mar  17  at 13:08
Дата публикации: Mar  17  at 13:08

Название статьи: Cross-Platform System Programming Guide for UNIX & Windows: Level 1
Автор: simonzolin
        Mar  17  at 09:21
Дата публикации: Mar  17  at 09:21

Название статьи: Journey to find a headset with a good side talk cancellation mic for calls in an open office
Автор: Murz
        Mar  17  at 09:04
Дата публикации: Mar  17  at 09:04

Название статьи: PostgreSQL 16: Part 4 or CommitFest 2023-01
Автор: kaze_no_saga
        Mar  10  at 16:27
Дата публикации: Mar  10  at 16:27

Название статьи: Onchain Analysis in Simple Terms
Автор: pazlvbanke
        Mar  9  at 16:48
Дата публикации: Mar  9  at 16:48

Название статьи: What is Information Technologies? Hard to gets in? Choosing a direction/profession and your first programming language
Автор: mastervlados
        Mar  6  at 15:56
Дата публикации: Mar  6  at 15:56

Название статьи: Autofill input fields in Android WebView
Автор: chugunovr
        Mar  5  at 21:44
Дата публикации: Mar  5  at 21:44

Название статьи: Microfrontend. Server fragments — frontend as it supposed to be
Автор: EgorVoronov
        Mar  5  at 21:42
Дата публикации: Mar  5  at 21:42

Название статьи: Writing The Matrix in Python: easy guide
Автор: AKlimenkov
        Mar  4  at 19:33
Дата публикации: Mar  4  at 19:33

Название статьи: DSL (domain-specific language) implementation with macros
Автор: rsashka
        Mar  4  at 14:42
Дата публикации: Mar  4  at 14:42

Название статьи: Use of Python to write plugins for GIMP
Автор: AmiraB2
        Mar  4  at 14:38
Дата публикации: Mar  4  at 14:38

Название статьи: Will transport planners lose their jobs as AI becomes smarter?
Автор: Badianov
        Mar  1  at 02:14
Дата публикации: Mar  1  at 02:14
```
