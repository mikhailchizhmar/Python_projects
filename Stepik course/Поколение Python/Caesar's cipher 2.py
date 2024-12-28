ru_upper = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
ru_lower = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
en_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
en_lower = 'abcdefghijklmnopqrstuvwxyz'


def encrypt(string, key, lang):
    result = ''
    for i in range(len(string)):
        if string[i].isalpha():
            if string[i].isupper():
                if lang == 'анг':
                    index = en_upper.find(string[i])
                    result += en_upper[(index + key) % 26]
                if lang == 'рус':
                    index = ru_upper.find(string[i])
                    result += ru_upper[(index + key) % 32]
            else:
                if lang == 'анг':
                    index = en_lower.find(string[i])
                    result += en_lower[(index + key) % 26]
                if lang == 'рус':
                    index = ru_lower.find(string[i])
                    result += ru_lower[(index + key) % 32]
        else:
            result += string[i]
    return result


def decrypt(string, key, lang):
    result = ''
    for i in range(len(string)):
        if string[i].isalpha():
            if string[i].isupper():
                if lang == 'анг':
                    index = en_upper.find(string[i])
                    result += en_upper[(index - key) % 26]
                if lang == 'рус':
                    index = ru_upper.find(string[i])
                    result += ru_upper[(index - key) % 32]
            else:
                if lang == 'анг':
                    index = en_lower.find(string[i])
                    result += en_lower[(index - key) % 26]
                if lang == 'рус':
                    index = ru_lower.find(string[i])
                    result += ru_lower[(index - key) % 32]
        else:
            result += string[i]
    return result


print('Шифр Цезаря')
while True:
    mode = input('Выберите режим: ш - шифрование, д - дешифрование\n')
    language = input('Выберите язык: рус - русский, анг - английский\n')
    k = int(input('Введите шаг сдвига\n'))
    text = input('Введите текст\n')
    if mode == 'ш':
        new_text = encrypt(text, k, language)
        print('Результат:', new_text)
    elif mode == 'д':
        new_text = decrypt(text, k, language)
        print('Результат:', new_text)
    else:
        print('Некорректный ввод режима!')
    decision = input('Продолжить? д - да, н - нет\n')
    if decision == 'н':
        print('До свидания!')
        break
