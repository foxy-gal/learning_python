""""Игра угадай число"""
import numpy as np #подключение библиотечки
number = np.random.randint(1, 101) #загадываем число

count = 0

while True:
    count+=1
    predict_number = int(input("Угадай число от 1 до 100:"))

    if number > predict_number:
        print("Число должно быть больше")

    elif number < predict_number:
        print("Число должно быть меньше")

    else:
        print(f"Вы угадали число! Это число = {number}. Угадано за {count} попыток")