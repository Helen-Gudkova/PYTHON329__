# lesson_12
# РАЗБОР ДОМАШНЕГО ЗАДАНИЯ №9 и №10

"""
# Домашнее задание 📃

Сегодня мы начинаем работать над игрой в города. Нашим оппонентом будет компьютер, в распоряжении которого весь список городов в РФ! 🧠
**Делаем MVP игры!**

6. Придумайте, как можно реализовать проверку условий выполнения игры
 (подходит ли ответ пользователя, согласно тому городу, который озвучил компьютер?)

7. Пусть компьютер теперь сделает свой ход. Поищет город,
который кончается на последнюю букву того города, который назвали вы.

8. Если такой город есть - повторите цикл.
9. В конце игры, объявите победителя.
# Критерии проверки 👌

- У вас должна получится **рабочая** игра в города с компьютером.
- Пробегитесь по моему алгоритму. Вероятно, в нём есть ошибка. Но если вы выполнили рабочую игру, то смогли найти её 👼
- Нейминг переменных (хорошие читаемые имена, подходящие по смыслу)
- PEP-8
"""
import json
from typing import Any

from cities import cities
from pprint import pprint


# sities_set = set()
#
# for city in cities:
#     sities_set.add(city['name'])
#
# # Запись сета в JSON файл
# with open('cities_set.json', 'w', encoding='utf-8') as file:
#     json.dump(list(sities_set), file, ensure_ascii=False, indent=4)

# BAD_FIRST_LETTERS = f'Вы назвали город которого нет'
# COMPUTER_WIN = f'Компьютер победил, назвав город'
#
# # Функция чтения сета из JSON файла
# def read_from_json(file_name, encoding='utf-8'):
#     with open(file_name, 'r', encoding=encoding) as file:
#         return json.load(file)
#
#
# # Функция записи в JSON файл
# def write_to_json(file_name, data, encoding='utf-8'):
#     with open(file_name, 'w', encoding=encoding) as file:
#         json.dump(data, file, ensure_ascii=False, indent=4)
#
#
# # Функция логирования
# def get_log_writer(data, file_name, encoding='utf-8'):
#     print(data)
#     write_to_json(file_name, data, encoding=encoding)
#
#
# # Функция логирования побед. Открывает файл лога побед, читает его, и добавляет в него последнюю победу
# # Лог побед - список. Он не должен быть более 5 элементов длиной
#
# def get_log_writer_win(data, file_name='win_log.md', encoding='utf-8'):
#     win_log = read_from_json(file_name, encoding=encoding)
#     if win_log and len(win_log) >= 5:
#         win_log[0] = data
#     else:
#         win_log.append(data)
#     write_to_json(file_name, win_log, encoding=encoding)

#
# cities_set = set(read_from_json('cities_set.json'))
#
# computer_city = None
# bad_letters = ('ь', 'ы', 'ъ')
# last_letter_index = -1
#
# while True:
#     user_city = input('Введите город: ')
#
#     if user_city == 'стоп':
#         print('Вы проиграли')
#         break
#
#     # Проверяем на окончание плохой буквы
#     if user_city[last_letter_index] in bad_letters:
#         print(f'Пожалуйста выберите другую букву. {user_city[last_letter_index]}')
#         continue
#
#     # Проверяем ответ компьютера
#     if computer_city:
#         if user_city[0].lower() != computer_city[last_letter_index].lower():
#             print(f'Вы проиграли. Ваш ответ не начинается на букву {computer_city[last_letter_index]}')
#             break
#
#     # Проверяем на наличие в сете городов
#     if user_city in cities_set:
#         print(f'Город: {user_city} есть в списке')
#         # Удаляем город из сета
#         cities_set.remove(user_city)
#
#     else:  # Если нет, то играем дальше
#         print(f'Города {user_city} нет в списке. Вы проиграли')
#         # Логируем результат матча
#         get_log_writer_win(f'Пользователь проиграл. Города {user_city} нет в списке\n'
#                            f'А компьютер победил, назвав город {computer_city}\n'
#                            f'--------------------------\n\n')
#         break
#
#     # Ход компьютера
#
#     # Получаем последнюю букву в названии города
#     last_letter = user_city[last_letter_index].lower()
#     # Поиск города в сете
#     for city in cities_set:
#         if city[0].lower() == last_letter and city[-1].lower() not in bad_letters:
#             print(f'Компьютер называет город: {city}')
#             computer_city = city
#             cities_set.remove(city)
#             break
#
#     else:
#         print('Вы победили! Компьютер не смог назвать город')
#         # Логируем результат матча
#         get_log_writer_win(f'Пользователь победил. Город {user_city} Компьютер не смог назвать город\n')
#         # last_letter_index -= 1
#         pass
#
#
# def main():
#     city_set = set(read_from_json('cities_set.json'))
#     user_city = None
#
#     # Пользовательский ввод
# # Функция логирования
#   pass
#
#
#
# main()

# ФУНКЦИИ
def get_som():
    str = 'Hello'
    return str


def say_it(string):
    if string == 'Hello':
        return 'Привет'
    elif string == 'Bye':
        return 'Пока'
    else:
        return 'Не понимаю'


result = say_it('asdf')
print(result)


# Практика - расшифровка статус-кодов HTTP
# 1xx: Informational (информационные): 100 Continue, 101 Switching Protocols, 102 Processing
# 2xx: Success (успешно): 200 OK, 201 Created, 204 No Content
# 3xx: Redirection (перенаправление): 301 Moved Permanently, 302 Found, 304 Not Modified
# 4xx: Client Error (ошибка клиента): 400 Bad Request, 401 Unauthorized, 403 Forbidden, 404 Not Found
# 5xx: Server Error (ошибка сервера): 500 Internal Server Error, 502 Bad Gateway, 503 Service Unavailable, 504 Gateway Timeout

# Функция расшифровки статус-кода, принимает на вход код, и возвращает расшифровку
# Достаточно сделать проверку ТОЛЬКО НА ПЕРВУЮ ЦИФРУ
# def get_status_code(code):
# Попробуйте сделать на match case

def get_status_code(code: int) -> str:
    """
    Функция расшифровки статус-кода, принимает на вход код, и возвращает расшифровку
    :param code: Статус-код ответа HTTP
    :return: Расшифровка статус-кода
    """
    match code:
        case int(1):
            return 'Informational (информационные)'
        case int(2):
            return 'Success (успешно)'
        case int(3):
            return 'Redirection (перенаправление)'
        case int(4):
            return 'Client Error (ошибка клиента)'
        case int(5):
            return 'Server Error (ошибка сервера)'
        case _:
            return 'Неизвестный код'


user_input = int(input('Введите код: '))
print(get_status_code(user_input))

# Практика №2
"""
Напишите функцию, которая на входе принимает строку.

Возвращает словарь, в котором ключ - это буква, а значение - это количество повторений этой буквы в строке.
sequence.count(element) - возвращает количество элементов element в последовательности sequence

# def letter_counter(string):

# сложная версия
Сделайте документацию и аннотацию типов
Подумайте, как сделать так, чтобы цикл работал меньше
"""


def letter_counter(string: str) -> dict:
    """
    Функция подсчета количества букв в строке
    :param string: Строка для подсчета букв
    :return: Словарь. Ключ - буква, значение - число
    """
    res_dict = {}

    str_set = set(string)
    for letter in str_set:

        if letter != ' ':
            count = string.count(letter)
            res_dict[letter] = count

    return res_dict


string = 'Аргентина манит негрА Аргентина манит негрА Аргентина манит негрА Аргентина манит негрА' \
         'Аргентина манит негрА Аргентина манит негрААргентина манит негрА '

some_float = 1, 0
print(type(some_float))
print(letter_counter(string))

"""
Напишите функцию, которая принимает словарь и значение. 
Функция должна вернуть ключ и значение, соответствующий переданному значению.
"""


def get_key_by_value(dict_: dict, value: Any) -> dict:
    """
    Функция возвращает ключ и значение, соответствующий переданному значению.
    :param dict_: Словарь
    :param value: Значение
    :return: Словарь
    """
    for key, val in dict_.items():
        if val == value:
            return {key: val}


# Тестовый датасет
full_dict = {
    'title': 'Железный человек',
    'year': 2008,
    'director': 'Джон Фавро',
    'screenwriter': 'Марк Фергус и Хоук Остби, Артур Маркам и Мэтт Холлоуэй',
    'producer': 'Ави Арад и Кевин Файги',
    'stage': 'Первая фаза'
}

print(get_key_by_value(full_dict, 'Джон Фавро'))
