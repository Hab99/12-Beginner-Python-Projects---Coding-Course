#guess_the_number_computer / Adivinhe o número computador
import random

def guess (x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input('Adivinhe um número entre 1 e 10: '))
        if guess < random_number:
            print('Desculpe, tente novamente. Muito baixo.')
        elif guess > random_number:
            print('Desculpe, tente novamente. Muito alto.')
        
    print(f'Parabéns! Você acertou o número {random_number}')

guess(10)