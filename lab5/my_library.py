

def task5_1(s):
    '''
    Дана строка символов. Вывести часть этой строки, предшествующую первой
    запятой. Если в тексте нет запятой, то сообщить об этом.

    :param s: строка символов
    :return: часть этой строки, предшествующую первой запятой
    '''
    zap = s.find(',')
    if zap == -1:
        print('Запятой нет')
    else:
        s2 = s[0:zap]
        return s2


def task5_2(text):
    '''
    Дан текст из слов, разделенных пробелами. Вывести на экран все слова,
    совпадающие с последним словом фразы. Если таких слов нет, выдать
    соответствующее сообщение

    :param text:
    :return: None
    '''
    words = text.split()

    last_word = words[-1] if words else ""

    matching_words = []

    for word in words:
        if word == last_word:
            matching_words.append(word)

    if len(matching_words) > 1:
        print("Совпадающие слова:", ' '.join(matching_words[:-1]))
    else:
        print("Совпадающих слов нет.")


def task5_3(s):
    '''
    Дана строка символов. Инвертировать все слова нечетной длины,
    начинающиеся на гласную букву, последовательность слов сохранить

    :param s: вводимая строка
    :return result:инвертированные слова
    '''
    s = s.split()
    s2 = []
    for i in s:
        if len(i) % 2 != 0:
            if i[0] in 'аеёиоуыэюяАЕЁИОУЫЭЮЯ':
                i = i[::-1]
                s2.append(i)
    result = ' '.join(s2)
    return result


def task5_4(text):
    '''
    Текст шифруется по следующему правилу: из исходного текста выбирается
    1, 4, 7, 10-й и т.д. (до конца текста) символы, затем 2, 5, 8, 11-й и т.д. (до конца
    текста) символы, затем 3, 6, 9, 12-й и т.д. Зашифровать заданный текст.

    :param text: текст для шифровки
    :return encrypted_text: зашифрованный текст
    '''

    encrypted_text = ""

    length = len(text)

    i = 0
    while i < length:
        encrypted_text += text[i]
        i += 3

    i = 1
    while i < length:
        encrypted_text += text[i]
        i += 3

    i = 2
    while i < length:
        encrypted_text += text[i]
        i += 3

    return encrypted_text



def task5_5(ip_address):
    '''
    Составить регулярное выражение, определяющее является ли заданная
    строка IP адресом, записанным в десятичном виде.
    – пример правильных выражений: 127.0.0.1, 255.255.255.0.
    – пример неправильных выражений: 1300.6.7.8, abc.def.gha.bcd.

    :param ip_address: вводимый ip адрес
    :return: None
    '''
    import re

    pattern = r'^(?!\.)((^|\.)(\d|[1-9]\d|1\d\d|2[0-4]\d|25[0-5])){4}$'

    if re.match(pattern, ip_address):
        print("Это корректный IP-адрес.")
    else:
        print("Это некорректный IP-адрес.")\



def task5_6(s):
    '''
    Строки, содержащие слово внутри произвольного текста, не содержащего
    скобок, в скобках. Пример строк, которые подходят: «good (excellent) phrase»,
    «good (too bad) phrase», «good ((recursive)) phrase». Пример строк, которые не
    подходят: «word () is not () in brackets», «bad (() recursive) phrase», «no brackets here».

    :param s: вводимая строка
    :return: None
    '''
    import re

    pattern = r"good \(+(.*?)\)+ phrase"

    if re.match(pattern, s):
        print("Строка подходит:", s)
    else:
        print("Строка не подходит.")



def task5_7(s):
    '''
    Заменить все числа кратные 10 на их частное от деления на 10. В этой задаче
    на вход подаются числа, разделенные пробелами. Примеры замен: «1 2 10 12
    20 123 239 566 12800» → «1 2 1 12 2 123 239 566 1280».

    :param s: вводимые числа
    :return s2: измененная строка
    '''
    import re

    def replace(match):
        return str(int(match.group(0)) // 10)

    s2 = re.sub(r'\b(\d+0)\b', replace, s)

    return s2







