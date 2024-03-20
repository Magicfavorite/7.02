"""Написать игру «Быки и коровы». Программа «загадывает» четырёхзначное число и играющий должен
угадать его. После ввода пользователем числа программа
сообщает, сколько цифр числа угадано (быки) и сколько
цифр угадано и стоит на нужном месте (коровы). После
отгадывания числа на экран необходимо вывести количество сделанных пользователем попыток. В программе
необходимо использовать рекурсию."""

import random

def bulls_and_cows(guess, secret):
    bulls = 0
    cows = 0
    for i in range(len(guess)):
        if guess[i] == secret[i]:
            bulls += 1
        elif guess[i] in secret:
            cows += 1
    return bulls, cows

def play_bulls_and_cows():
    secret_number = random.randint(1000, 9999)
    guess = ''
    attempts = 0
    while guess != secret_number:
        attempts += 1
        guess = input(f"Введите четырехзначное число: ")
        while len(guess) != 4:
            print("Введено число не четырехзначное. Пожалуйста, введите четырехзначное число.")
            guess = input(f"Введите четырехзначное число: ")
        bulls, cows = bulls_and_cows(guess, str(secret_number))
        print(f"Быки: {bulls}, Коровы: {cows}")
    print(f"Вы угадали число за {attempts} попыток.")

play_bulls_and_cows()
