"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


def random_predict(number: int = 1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    boundary_min = 1 # задаем границы интервала угадывания
    boundary_max = 100
          
    while True:
        count += 1 # увеличиваем число попыток на 1
        predict_num = (boundary_min + boundary_max)//2  # задаем predict_number как целую часть среднего арифметического границ интервала
        if number == predict_num:
            break  # выход из цикла если угадали 
        if predict_num > number: # если предполагаемое число больше загаданного
            boundary_max = predict_num-1 # меняем верхнюю границу интервала угадывания   
        else: # если предполагаемое число меньше загаданного
            boundary_min = predict_num+1 # меняем нижнюю границу интервала угадывания            
    return count

def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел
    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(random_predict)
