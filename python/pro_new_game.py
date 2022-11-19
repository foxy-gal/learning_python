import numpy as np

def random_predict(number:int=1) -> int:
    """_summary_

    Args:
        number (int, optional): _description_. Defaults to 1.

    Returns:
        int: _description_
    """


    count = 0

    while True:
        count += 1
        predict_number = np.random.randint(1, 101) # предполагаемое число
        if number == predict_number:
            break # выход из цикла, если угадали
    return(count)

print(f'Количество попыток: {random_predict()}')