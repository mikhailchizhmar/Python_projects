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


copy_s = input()
s = copy_s.split()
res_str = ''

for i in range(len(s)):
    count = 0
    for j in range(len(s[i])):
        if s[i][j].isalpha():
            count += 1
    res_str += encrypt(s[i], count, 'анг')

for i in range(len(copy_s)):
    if copy_s[i] == ' ':
        res_str = res_str[:i] + ' ' + res_str[i:]

print(res_str)
