"""

# Разбор HW №14 (Палиндром)
Функция возвращает данные в формате списка словарей, где ключ - проверяемое значение,
а значение ключа - булев тип.

```python
result = [
Напишите функцию, которая принимает `*args` строк, и производит их проверку на палиндромность.
		  {'строка 1': True},
		  {'строка 2': False}
]
```
- Проведите тестирование.
- Сделайте пользовательский ввод, превратите его в список.
- Затем распакуйте список в функцию проверки на палиндром, при вызове этой функции.

"""
from pprint import pprint


def check_palindromes(*strings):
    result = []
    for string in strings:
        if string == string[::-1]:
            result.append({string: True})
        else:
            result.append({string: False})
    return result


# Проверяем, как именно работает insert
# Методы добавления элементов в список
# append - добавляет элемент в конец списка
# insert - добавляет элемент в список по индексу
# extend - добавляет элементы в конец списка из другого списка

def check_palindromes_test_version(*strings):
    result = []
    for string in strings:
        if string == string[::-1]:
            result.insert(3, {string: True})
        else:
            result.insert(3, {string: False})
    return result


# input_lst = input('Введите строки через запятую: ').split(',')
# print(check_palindromes(*input_lst))

# =========================================================
# Разбор HW №12 (Словарь сотрудников)
# Написать 3 функции
"""1 Пересечение списков
Напишите функцию, которая принимает два списка и возвращает новый список, 
содержащий только общие элементы."""


def intersection_short_version(lst1, lst2):
    return list(set(lst1) & set(lst2))


def intersection_long_version(lst1, lst2):
    set1 = set(lst1)
    set2 = set(lst2)
    intersection_set = intersection(set1, set2)
    result = list(intersection_set)
    return result


def intersection(lst1, lst2):
    result = []
    for element in lst1:
        if element in lst2:
            result.append(element)
    return result


# Задача 2 - проверка - сколько гласных и согласных в слове
"""Количество гласных и согласных Напишите функцию, которая 
принимает строку и возвращает количество гласных и согласных букв в ней."""

# VOWELS = ['а', 'е', 'ё', 'и', 'о',
#           'у', 'ы', 'э', 'ю', 'я']

# CONSONANTS = ['б', 'в', 'г', 'д', 'ж', 'з', 'й', 'к', 'л', 'м', 'н',
#               'п', 'р', 'с', 'т', 'ф', 'х', 'ц', 'ч', 'ш', 'щ']


# def count_vowels_and_consonants(word):
#     vowels = 0
#     consonants = 0
#     for letter in word:
#         if letter.lower() in VOWELS:
#             vowels += 1
#         elif letter.lower() in CONSONANTS:
#             consonants += 1
#     return vowels, consonants
#

# word_input = input('Введите слово: ')
# print(count_vowels_and_consonants(word_input))

# Задача 3
# Напишите функцию, которая принимает список строк и возвращает самую длинную строку из списка.

# def find_longest_string(lst):
#     longest_string = ''
#     for string in lst:
#         if len(string) > len(longest_string):
#             longest_string = string
#     return longest_string


# test_lst = ['1', '22', '333', '4444', '55555', '66']

# print(find_longest_string(test_lst))

# =========================================================
# Разбор HW №15 (Разбивка MD файла)

MD_STRING = """
---
tags:
  - python329
journal: "[[PYTHON 329. Журнал]]"
type:
  - home work
block: python
hw_theme:
  - Markdown
  - functions
hw_num: 1
topic: Пишем функции для чтения, записи и добычи содержимого заголовков в Markdown файле
st_group: python 329
date: 2023-09-10
module: 8
lesson_no: 32
lesson_file: "[[Python 329. Python. Lesson 32]]"
---
# Домашнее задание 📃

Сегодня будет творческое задание. Представьте что вы закончили обучение, и пока ищете работу, подрабатываете на фрилансе.

Вы взяли, как кажется простой заказ. Написать несколько функций для работы с файлами Markdown.

Заказчик был не особо общителен, но он всё же дал сносное техническое задание.

# ТЗ от заказчика 😎

Напишите модуль для работы с Markdown файлами. Он должен состоять из документерованных функций, которые помогут мне читать, записывать и перезаписывать Markdown файлы.

- Функция чтения MD файла. Принимает строку с именем файла, открывает файл на чтение (так же как TXT), возвращает всё содержимое файла одной строкой
- Функция разбивки MD файла по заголовкам. Принимает результат работы прошлой функции и разбивает строку, в которой содержится весь файл на список. Отдает список. Каждый элемент списка = Заголовок MD файла и содержимое
- Функция записи. Принимает строку и записывает MD файл
"""

# Нам надо получить список в котором каждый элемент будет заголовок + содержимое

DELIMITER = '#'
TEMP_LST = MD_STRING.split(DELIMITER)
# print(TEMP_LST)


# def split_md_file_to_dict(file_string: str) -> dict:
#     """
#     Функция, которая принимает строку с прочитанным файлом в формате MD.
#     Возвращает словарь, в котором ключи - это названия метаданных, а значения - сами метаданные.
#     """
#     metadata_end = file_string.index("---", 3)  # Находим конец метаданных 3 - это начало "---"
#     metadata = file_string[3:metadata_end].strip()  # Обрезаем начало и конец метаданных
#     text = file_string[metadata_end + 3:].strip()  # Обрезаем начало текста
#
#     metadata_dict = yaml.safe_load(metadata)
#
#     return {"metadata": metadata_dict, "text": text}


def split_md_file_to_list(file_string: str) -> list:
    """
    Функция, которая принимает строку с прочитанным файлом в формате MD.
    Возвращает список, в котором каждый элемент списка - это заголовок и его содержимое.
    Функция не учитывает frontmatter.
    Функция добавляет только заголовки первого уровня и всё их содержимое
    """
    # Разделяем строку по символу #
    file_lst = file_string.split('#')
    # Удаляем первый элемент списка, так как он не содержит заголовок
    file_lst.pop(0)
    # Проходим циклом по списку и добавляем в начало символ #
    for i in range(len(file_lst)):
        file_lst[i] = '#' + file_lst[i]
    # Возвращаем список
    return file_lst


# Сделаем одну функцию, которая вернет список разделов - заголовок и содержимое (метаданные просто уберем)
# Удаляем полностью метадату коротая начинается с --- и заканчивается ---
# Находим конец метадаты
metadata_end = MD_STRING.index("---", 3)
# Обрезаем начало и конец метадаты
text = MD_STRING[metadata_end + 3:].strip()
# Разделяем строку по символу #
file_lst = text.split('#')

# Удаляем первый элемент списка, так как он не содержит заголовок
file_lst.pop(0)
# Проходим циклом по списку и добавляем в начало символ #
for i in range(len(file_lst)):
    file_lst[i] = '#' + file_lst[i]
# Возвращаем список
# print(file_lst)


# Вариант Андрея - разбивка по ---

# --------------------------------------------------
# Анонимные функции (лямбда функции)

# Преимущества:
# - не нужно придумывать имя
# - не нужно писать return
# - можно использовать внутри других функций
# - однострочные

# Недостатки:
# - нельзя написать докстринг
# - нельзя написать декоратор
# - нельзя написать многострочную функцию
# - нельзя использовать приравнивание, return, yield

# Синтаксис:
# lambda arguments: expression

# Примеры:

def func1(x):
    return x + 1


func2 = lambda x: x + 1

print(func1(1))
print(func2(1))


# map - применяет функцию к каждому элементу итерируемого объекта
user_int_input = ['1', '2', '3', '4', '5']

# Проходим map по списку и применяем к каждому элементу функцию int
user_int_input = list(map(int, user_int_input))

# Делаем lambda + map
user_int_input = list(map(lambda x: int(x)+100, user_int_input))
print(user_int_input)