
"""
Главный модуль программы
Осуществляет выполнение выбранной из меню задачи, посредством вызова
соответствующей подпрограммы
Перед вызовом запрашивает нужные исходные данные подпрограммы
"""

from lab5.my_library import task5_1, task5_2, task5_3, task5_4, task5_5, task5_6, task5_7


def menu():
    """
    Функция предлагает выбор номера задания\n
    :param : нет передаваемых параметров
    :return: choice_task - выбранный номер задания
    """

    choice_task = int(input('Выберите номер задания в лабораторной работе: '))

    return choice_task

if __name__ == '__main__':
    while True:
        choice = menu()

        match choice:

            case 1:
                s = input('Введите строку: ')
                print(task5_1(s))

            case 2:
                text = input('Введите текст: ')
                task5_2(text)

            case 3:
                s = input('Введите строку: ')
                print(task5_3(s))

            case 4:
                text = input("Введите текст: ")
                print(f'"Зашифрованный текст: "{task5_4(text)}')

            case 5:
                ip_address = input("Введите IP-адрес: ")
                task5_5(ip_address)

            case 6:
                s = input("Введите строку: ")
                task5_6()
            case 7:
                s = input('Введите через пробел: ')
                print(task5_7(s))

            case _:
                    break
        if input('Продолжить? Да/Нет: ') == 'Нет'.lower(): break

