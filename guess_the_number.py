import random as r

def define_border():
    border = input('Выбери промежуток от 1 до N. Введи N: ')
    while not border.isdigit():
        print('А, может быть, введёшь целое число?\n')
        border = input('Выбери промежуток от 1 до N. Введи N: ')
    return int(border)


def is_valid(string, n):
    return string.isdigit() and 0 < int(string) <= n


def compare_number(n):
    random_number = r.randint(1, n)
    counter = 0
    while True:
        number = input(f'Угадай число от 1 до {n}: ')
        counter += 1
        if is_valid(number, n):
            number = int(number)
            if number == random_number:
                print('Вы угадали, поздравляем!')
                print(f'Количество попыток:{counter}')
                break
            elif number < random_number:
                print('Твоё число меньше загаданного, попробуйте ещё разок')
            else:
                print('Твоё число больше загаданного, попробуйте ещё разок')
        else:
            print(f'А, может быть, введёшь целое число от 1 до {n}?\n')
            continue

def play_game():
    n = define_border()
    compare_number(n)

def next_game():
    string = input('Будем играть дальше? ')
    while string.lower() == 'да':
        play_game()
        string = input('Будем играть дальше? ')
    print('Спасибо, что играли в числовую угадайку! Ещё увидимся...')


print('Добро пожаловать в числовую угадайку!\n')
play_game()
next_game()