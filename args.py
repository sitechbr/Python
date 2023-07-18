#!/usr/bin/env python3
import sys

# получаем аргументы командной строки
args = sys.argv

# проверяем, что передано достаточное количество аргументов
if len(args) < 2:
    print("Необходимо передать аргументы командной строки")
    sys.exit(1)

# получаем первый аргумент - путь к файлу
file_path = args[1]

# открываем файл на чтение
try:
    with open(file_path, 'r') as f:
        for line in f:
            print(line.strip())
except FileNotFoundError:
    print("Файл не найден")
    sys.exit(1)
except:
    print("Произошла ошибка при чтении файла")
    sys.exit(1)
