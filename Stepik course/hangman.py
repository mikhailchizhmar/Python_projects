import random
word_list = ["виселица", "яблоко", "игра", "зонт", "кино"]


def get_word():
    return random.choice(word_list).upper()


def display_hangman(tries):
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                ''',
                # голова, торс, обе руки, одна нога
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                ''',
                # голова, торс, обе руки
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                ''',
                # голова, торс и одна рука
                '''
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                ''',
                # голова и торс
                '''
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                ''',
                # голова
                '''
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                ''',
                # начальное состояние
                '''
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                '''
    ]
    return stages[tries]


def play(word):
    word_completion = '_' * len(word)  # строка, содержащая символы _ на каждую букву задуманного слова
    guessed = False  # сигнальная метка
    guessed_letters = []  # список уже названных букв
    guessed_words = []  # список уже названных слов
    tries = 6  # количество попыток

    print('Давайте играть в угадайку слов!')

    while True:
        if tries == 0:
            print(display_hangman(tries))
            print('Вы проиграли(')
            print("Было загадано слово:", word)
            break
        print(display_hangman(tries))
        print(word_completion)
        print(f"Осталось попыток: {tries}")

        if guessed:
            print('Поздравляем, вы угадали слово! Вы победили!')
            break

        attempt = input('Введите букву или слово: ').upper()
        while not attempt.isalpha():
            attempt = input("Некорректный ввод! Попробуйте ещё раз: ").upper()
        if len(attempt) > 1:
            if attempt in guessed_words:
                print('Это слово уже было названо!')
            elif attempt == word:
                guessed = True
                word_completion = attempt
            else:
                guessed_words.append(attempt)
                tries -= 1
        else:
            if attempt in guessed_letters:
                print('Эта буква уже была названа!')
            else:
                guessed_letters.append(attempt)
                if attempt in word:
                    for i in range(len(word)):
                        if word[i] == attempt:
                            word_completion = word_completion[:i] + attempt + word_completion[i + 1:]
                else:
                    tries -= 1

        if word_completion == word:
            guessed = True


while True:
    play(get_word())
    decision = input("Хотите сыграть ещё? д - да, н - нет\n")
    if decision == "н":
        print("До свидания!")
        break
