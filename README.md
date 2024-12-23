task5_5()
^ - Начало строки.
(?!\.) - Отрицательный просмотр вперед, который гарантирует, что строка не начинается с точки (.).
((^|\.)(\d|[1-9]\d|1\d\d|2[0-4]\d|25[0-5])){4} - Основная часть, которая проверяет наличие четырех октетов IP-адреса:
(^|\.)(...) - Каждый октет может начинаться либо с начала строки (^), либо с точки (\.).
(\d|[1-9]\d|1\d\d|2[0-4]\d|25[0-5]) - Проверяет, что октет соответствует одному из следующих условий:
\d - одна цифра (0-9).
[1-9]\d - две цифры, где первая не нулевая (10-99).
1\d\d - три цифры, начинающиеся с 1 (100-199).
2[0-4]\d - три цифры, начинающиеся с 2 и следующими цифрами от 0 до 4 (200-249).
25[0-5] - три цифры, начинающиеся с 25 и следующей цифрой от 0 до 5 (250-255).
{4} - Указывает, что предыдущая группа (октет) должна повторяться ровно 4 раза.
$ - Конец строки.

task5_6()
good - Начало шаблона, которое ищет точное совпадение со словом "good".
$ - Экранированная открывающая скобка (. Поскольку скобка имеет специальное значение в регулярных выражениях, она экранируется с помощью обратной косой черты \, чтобы искать именно символ (.
+ - Квантификатор, который указывает, что предыдущий символ (в данном случае \() должен встречаться один или более раз. Это означает, что мы ищем одну или несколько открывающих скобок.
(.*?) - Группа захвата:
. - Соответствует любому символу, кроме символа новой строки.
* - Квантификатор, который указывает, что предыдущий символ (в данном случае .) может встречаться ноль или более раз.
? - Указывает, что квантификатор * должен быть "ленивым" (или "нежадным"), что означает, что он будет захватывать как можно меньше символов, чтобы соответствовать остальной части шаблона. Это позволяет захватить только те символы, которые находятся между открывающими и закрывающими скобками.
$+ - Экранированная закрывающая скобка ), которая также может встречаться один или более раз. Это означает, что мы ищем одну или несколько закрывающих скобок.
 phrase - Завершает шаблон, ищет точное совпадение со словом "phrase", которое должно следовать за закрывающими скобками.

task5_7()
re.sub(): Это функция, которая заменяет все вхождения шаблона (регулярного выражения) в строке на заданное значение.
r'\b(\d+0)\b': Это регулярное выражение, которое ищет числа, оканчивающиеся на ноль.
\b — это граница слова, которая гарантирует, что совпадение будет найдено только в начале или в конце слова.
(\d+0) — это группа, которая ищет одну или более цифр (\d+), за которыми следует ноль (0). Знак + означает "один или более раз".
В итоге, это выражение будет находить такие числа, как 10, 20, 300, и т.д.
replace: Это функция или строка, которая будет использоваться для замены найденных совпадений. Важно, чтобы replace была определена ранее в коде.
s: Это строка, в которой будет производиться поиск и замена.