# Разбор ДЗ с Марвел (поиск по словарю)
# PYTHON 329 HW №8
"""
# Домашнее задание 📃

1. Сохраните этот датасет в отдельный файл
2. Создайте второй файл в проекте
3. Импортируйте датасет в основной файл `from filename import your_dict`
4. Можете приступать к ДЗ 🙂

Мы будем искать подборку фильмов по вселенной Марвел. Пользователь вводит цифрами фазу (только одну).

Например `2`

Мы сверяемся со словарём (вам нужно будет его написать) где ключи - это цифры, а значения записаны строковым типом (так, как это написано в нашей базе)

Например

```python
stage = {
		 1:"Первая фаза",
		 2: "Продолжите дальше :)"
}
```
Сверьтесь с "базой" - сделайте такой словарик.

Если пользователь вводит строку - `raise TypeError` и пишем что ожидаем получить от него цифру

Если пользователь вводит несуществующий номер - делаем ему `raise ValueError` и пишем что такой фазы не существует.

Если запрашиваемая фаза есть в ключах нашего словаря, мы вытаскиваем значения в виде строки, например `Первая фаза` и делаем поиск по нашей базе.

Обратите внимание на структуру документа. Вам нужно будет работать с вложенным словарём!

Удачи!!! 🌞

# Критерии проверки 👌

1. Есть импорт переменной с "базой"
2. Есть словарь с фазами, который вы сделали сами
3. Есть `raise TypeError` при вводе чего-то отличного от числа
4. Есть `raise ValueError` при вводе несуществующей фазы
5. Есть поиск в цикле (или генератором) по фильмам
6. Есть успешный поиск с принтом (в любом виде, строка, список, что-угодно)
7. pep8
8. Нейминг переменных


"""

# stage = {
#     1: "Первая фаза",
#     2: "Вторая фаза",
#     3: "Третья фаза",
#     4: "Четвёртая фаза",
#     5: "Пятая фаза",
#     6: "Шестая фаза",
# }

# Пользователь вводит цифрами фазу (только одну).
# user_input = input(
#     "Введите номер фазы от 1 до 6: ")  # Можно сделать блок try-except, и в блоке except вызывать исключение ValueError
# Проверяем ввод пользователя на тип данных (методом строк) - если проверка не пройдена, то вызываем исключение
# TypeError Проверка на то, что введен верный диапазон значений. (Либо интуем и проверяем диапазон), либо проверяем
# введенное значение на наличие в словаре
# str_stage = stage.get(int(user_input))  # Фаза в виде строки - "Первая фаза"
# results = []

# for item in full_dict.values():
#     if item['stage'] == str_stage:
#         results.append(item['title'])

# Генератор списка
# results = [item['title'] for item in full_dict.values() if item['stage'] == str_stage]

# print(", ".join(results))  # Выводим результат в виде строки

# Чтение и запись в файл
# UTF-8, windows-1251, ascii

# file = open("my_file.txt", "w")  # Открываем файл для записи
# file.write("Привет, мир!")       # Записываем текст в файл
# file.close() # Закрываем файл. Важно! Потому что файл может быть занят другим процессом, и если мы не закроем его


# ФЛАГИ ОТКРЫТИЯ ФАЙЛА
# r - read (чтение) - Если файла нет, то будет ошибка
# w - write (запись) - Если файла нет, то он будет создан, или перезаписан
# a - append (дозапись) - Если файла нет, то он будет создан, или дозаписан
# b - binary (бинарный режим) - Для работы с изображениями, видео, аудио

# Работа с контекстным менеджером (with)

# message = """
# Привет, мир!\n
# Мы изучаем файлы в Python\n
# """
#
# with open("my_file.txt", "w", encoding='UTF-8') as file:
#     file.write(message)

# Построчное чтение файла txt через контекстный менеджер
# readline() - читает одну строку
# readlines() - читает все строки и возвращает список строк

# with open("my_file.txt", "r", encoding='UTF-8') as file:
#     for line in file:
#         print(line)
#
# # Чтение файла целиком через метод readlines()
# with open("my_file.txt", "r", encoding='UTF-8') as file:
#     lines = file.readlines()
#
# print([line.strip() for line in lines])

# Построчная запись в файл
# some_str = ['Ещё одна строка', 'И ещё одна строка']
# with open("my_file.txt", "a", encoding='UTF-8') as file:
#     for line in some_str:
#         file.write(line + '\n')


# Уже изучили
# 1. Открытие файла
# 2. Запись в файл
# 3. Чтение файла
# 4. Построчное чтение файла
# 5. Построчная запись в файл
# 6. Контекстный менеджер

# РАБОТА С JSON
# JSON - JavaScript Object Notation
# JSON - это формат данных, который используется для
# обмена данными между различными языками программирования. Back-end и Front-end

# Методы для работы с JSON

# Работаем со строками
# json.dumps() - преобразует объект Python в строку JSON
# json.loads() - преобразует строку JSON в объект Python
# Работаем с файлами
# json.dump() - записывает объект Python в файл в формате JSON
# json.load() - читает JSON из файла и преобразует в объект Python

# Пример записи данных в файл в формате JSON
#
# with open("my_file.json", "w", encoding="utf-8") as file:
#     json.dump(full_dict, file) # 2 аргумента. 1. Словарь, 2. Файл


# with open("my_file.json", "w", encoding="utf-8") as file:
#     # ensure_ascii=False - отключает кодировку в формате ASCII
#     json.dump(full_dict, file, ensure_ascii=False)  # 2 аргумента. 1. Словарь, 2. Файл
#
# with open("cities.json", "w", encoding="utf-8") as file:
#     # ensure_ascii=False - отключает кодировку в формате ASCII
#     # indent=1 - отступы в 1 пробел
#     json.dump(full_dict, file, ensure_ascii=False, indent=4)  # 2 аргумента. 1. Словарь, 2. Файл

# Для экселя надо использовать сторонние библиотеки
# Openpyxl - для работы с xlsx
# csv - comma separated values - для работы с csv

# Импортируем библиотеку для работы с csv
import csv

#  `csv.reader(file)`: Этот метод позволяет читать CSV файл построчно.
# - `csv.writer(file)`: Этот метод используется для записи данных в CSV файл.
# - `csv.DictReader(file)`: Этот метод позволяет читать CSV файл в виде словаря.
# - `csv.DictWriter(file, fieldnames)`: Этот метод используется для записи данных в CSV файл в виде словаря.

some_csv = """
Название,Цена,Категория
Яблоки,1.5,Фрукты
Молоко,2,Молочные продукты
Хлеб,0.8,Хлебобулочные изделия
"""

data = [
    ["Название", "Цена", "Категория"],
    ["Картофель", 0.5, "Овощи"],
    ["Сыр", 3, "Молочные продукты"]
]
# newline="" - убирает пустые строки
with open("../new_products.csv", "w", newline="", encoding="windows-1251") as file:
    writer = csv.writer(file)  # создаем объект writer
    writer.writerows(data)  # записываем данные в файл

# Делаем то же самое, но с разделителем;
with open("../new_products.csv", "w", newline="", encoding="windows-1251") as file:
    writer = csv.writer(file, delimiter=";")  # создаем объект writer
    writer.writerows(data)  # записываем данные в файл
#
# **Чтение CSV файла с помощью `csv.reader()`**
#
# ```python
# import csv
#
# with open("products.csv", "r", newline="", encoding="utf-8") as file:
#     reader = csv.reader(file)
#     for row in reader:
#         print(row)
# ```
#
# **Запись данных в CSV файл с помощью `csv.writer()`**
#
# ```python
# data = [
#     ["Картофель", 0.5, "Овощи"],
#     ["Сыр", 3, "Молочные продукты"]
# ]
#
# with open("new_products.csv", "w", newline="", encoding="utf-8") as file:
#     writer = csv.writer(file)
#     writer.writerows(data)
# ```
#
# **Чтение CSV файла как словаря с помощью `csv.DictReader()`**
#
# ```python
# with open("products.csv", "r", newline="", encoding="utf-8") as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         print(row["Название"], row["Цена"], row["Категория"])
# ```
#
# **Запись данных как словаря с помощью `csv.DictWriter()`**
#
# ```python
# data = [
#     {"Название": "Морковь", "Цена": 0.3, "Категория": "Овощи"},
#     {"Название": "Яйца", "Цена": 1.2, "Категория": "Продукты"}
# ]

# fieldnames = ["Название", "Цена", "Категория"]
#
# with open("new_products.csv", "w", newline="", encoding="utf-8") as file:
#     writer = csv.DictWriter(file, fieldnames=fieldnames)
#     writer.writeheader()
#     writer.writerows(data)

# url погодного API
# city = "Санкт-Петербург"
# wheater_url = fr'https://api.openweathermap.org/data/2.5/' \
#               fr'weather?q={city}&' \
#               fr'appid=23496c2a58b99648af590ee8a29c5348&units=metric&lang=ru'
#
# print(wheater_url)

# response = requests.get(wheater_url) # делаем запрос методом get
# data = response.json() # получаем данные в формате json. Метод json() возвращает словарь
# pprint(data)
#
# with open("weather.json", "w", encoding="utf-8") as file:
#     json.dump(data, file, indent=4, ensure_ascii=False)
# # indent=4 - отступы в 4 пробела
# # ensure_ascii=False - отключаем кодировку в ASCII (для кириллицы)
