import random

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
chars = ''


def is_valid_str(string):
    while True:
        if string == 'д' or string == 'н':
            break
        else:
            string = input('Некорректный ввод, введите "д" или "н" (д - да, н - нет)\n')
    return string


def is_valid_num(string):
    while True:
        if string.isdigit() and int(string) > 0:
            return int(string)
        else:
            print('Некорректный ввод, попробуйте ещё раз\n')


def delete_char(string, char):
    k = string.find(char)
    return string[:k] + string[k + 1:]


def delete_all_chars(string):
    if 'i' in string:
        string = delete_char(string, 'i')
    if 'l' in string:
        string = delete_char(string, 'l')
    if '1' in string:
        string = delete_char(string, '1')
    if 'L' in string:
        string = delete_char(string, 'L')
    if 'o' in string:
        string = delete_char(string, 'o')
    if 'O' in string:
        string = delete_char(string, 'O')
    if '0' in string:
        string = delete_char(string, '0')
    return string


def generate_password(quantity, length_of_password, string):
    password_list = []
    for i in range(quantity):
        key = random.sample(string, length_of_password)
        key = ''.join(key)
        password_list.append(key)
    return password_list


def output(mass):
    print('Ваши пароли:')
    for i in range(1, len(mass) + 1):
        print(str(i) + ": " + mass[i - 1])


name = input('Введите Ваше имя\n')
print('Привет, {}! Сейчас мы подберём тебе безопасные пароли.'.format(name))

amount = input('Введите количество паролей для генерации\n')
amount = is_valid_num(amount)

length = input('Введите длину одного пароля\n')
length = is_valid_num(length)

s = input('Включать ли цифры 0123456789? д - да, н - нет\n')
s = is_valid_str(s)
if s == 'д':
    chars += digits

s = input('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ? д - да, н - нет\n')
s = is_valid_str(s)
if s == 'д':
    chars += uppercase_letters

s = input('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz? д - да, н - нет\n')
s = is_valid_str(s)
if s == 'д':
    chars += lowercase_letters

s = input('Включать ли символы !#$%&*+-=?@^_? д - да, н - нет\n')
s = is_valid_str(s)
if s == 'д':
    chars += punctuation

s = input('Исключать ли неоднозначные символы il1Lo0O? д - да, н - нет\n')
s = is_valid_str(s)
if s == 'д':
    chars = delete_all_chars(chars)

passwords = generate_password(amount, length, chars)
output(passwords)
