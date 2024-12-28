import random

while True:
    while True:
        number = input('Введите правую границу для случайного выбора числа (целое число больше 1)\n')
        if number.isdigit() and int(number) > 0:
            number = int(number)
            break
        else:
            print('Некорректный ввод')


    def is_valid(s):
        if not s.isdigit() or int(s) > number or int(s) < 1:
            return False
        else:
            return True


    answer = random.randint(1, number)
    print('Добро пожаловать в числовую угадайку')
    tries = 0

    while True:
        guess = input('Введите целое число от 1 до {}\n'.format(number))
        tries += 1
        if not is_valid(guess):
            print('А может быть все-таки введем целое число от 1 до {}?'.format(number))
        else:
            guess = int(guess)
            if guess == answer:
                print('Вы угадали, поздравляем!')
                print('Количество попыток:', tries)
                break
            elif guess < answer:
                print('Ваше число меньше загаданного, попробуйте еще разок')
            else:
                print('Ваше число больше загаданного, попробуйте еще разок')

    decision = input('Хотите сыграть ещё?(введите "да" или "нет")\n')
    while True:
        if decision == "нет":
            break
        elif decision == "да":
            print("Продолжаем!")
            break

    if decision == "нет":
        break

print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
